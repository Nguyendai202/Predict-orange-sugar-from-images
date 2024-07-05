from fastapi import FastAPI, UploadFile, File
from segmentation.segmentation_orange import CamSegmentationModel
from regression.regression_orange import RegressionModel
from pipeline.pipelines import RegressionOrange
import zipfile
import os
import io
import tempfile
from typing import List
from definitions import (
    MODEL_SEGMENT_PATH,
    MODEL_REGRESSION_CONFIG_PATH,
    MODEL_REGRESSION_WEIGHT_PATH,
)
import uvicorn
import numpy as np
import cv2
import time
from starlette.responses import RedirectResponse
import concurrent.futures
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')
app_desc = """<h2>HUS-VNU</h2>"""
app = FastAPI(title="API Dự đoán độ đường cam Việt Nam", description=app_desc)
segment = CamSegmentationModel(MODEL_SEGMENT_PATH)
regress_model = RegressionModel(
    MODEL_REGRESSION_CONFIG_PATH, MODEL_REGRESSION_WEIGHT_PATH
).model
pipeline = RegressionOrange(regress_model)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post("/upload-images")
async def upload_images(files: List[UploadFile] = File(...)):
    predictions = {}
    times = []
    count_file = 0
    start_time_1 = time.time()
    try:
        for file in files:
            file_extension = os.path.splitext(file.filename)[1]
            if file_extension == '.zip':
                with tempfile.TemporaryDirectory() as temp_dir:
                    file_bytes = await file.read()
                    file_io = io.BytesIO(file_bytes)

                    with zipfile.ZipFile(file_io, "r") as zip_ref:
                        zip_ref.extractall(temp_dir)

                    for root, _, files in os.walk(temp_dir):
                        for filename in files:
                            count_file += 1
                            start_time = time.time()
                            image_path = os.path.join(root, filename)
                            image_array = cv2.imread(image_path)
                            with concurrent.futures.ThreadPoolExecutor() as executor:
                                features = [executor.submit(
                                    perform_prediction, image_array, filename)]
                                results = concurrent.futures.wait(features)
                                for f in results.done:
                                    predict, count_pass = f.result()
                                    predictions[filename] = predict.tolist()

                            elapsed_time = time.time() - start_time
                            times.append(elapsed_time)
            else:
                image_bytes = await file.read()
                image_array = np.frombuffer(image_bytes, dtype=np.uint8)
                img_bgr = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                predict, count_pass = perform_prediction(
                    img_bgr, file.filename)
                predictions[file.filename] = predict.tolist()
                elapsed_time = time.time() - start_time_1
                count_file += 1
                times.append(elapsed_time)
    except Exception as e:
        logging.error(f'Error uploading images from api: {str(e)}')
    return {
        "predictions": predictions,
        "times": times,
        "count_pass": count_pass,
        "count_file": count_file,
        "times": times,
    }


def perform_prediction(image, filename):
    try:
        image_segment = segment.image_segment(image)
        predict = pipeline.predict_segment(image_segment, filename)
        count_pass = pipeline.get_count()
    except Exception as e:
        logging.error(f'Error performing prediction from api: {str(e)}')
        predict = None
        count_pass = None
    return predict, count_pass


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
