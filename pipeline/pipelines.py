import numpy as np
import cv2
import pandas as pd
import re
import time
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')


class RegressionOrange(object):
    def __init__(self, regressionmodel):
        self.regressionmodel = regressionmodel
        self.count = 0
        self.results = []
        self.df = pd.read_csv("data\data_brix_new.csv")

    def predict_segment(self, image_segment, filename):
        try:
            image = image_segment
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = image / 255.0
            image = np.expand_dims(image, axis=0).astype(np.float32)
            start_time = time.time()
            predict = self.regressionmodel.predict(image)
            time_predict = time.time()-start_time
            value_predict = float(predict[0])  # predict[0]
            a1, b1 = self.get_a_b(filename)
            if a1 <= value_predict <= b1:  # A1
                self.count += 1
        except Exception as e:
            if self.regressionmodel is None:
                logging.error('Regression model is not set.')
            logging.error(
                f'Error predicting segment in regression_orange from regression: {str(e)}')
            predict = None
            time_predict = None
        # print('time predict:', time_predict)
        return predict

    def get_count(self):
        return self.count

    def get_a_b(self, filename):
        try:
            a = 0.0  # Giá trị mặc định cho a
            b = 0.0  # Giá trị mặc định cho b
            # Tìm chuỗi con chứa các kí tự chữ cái và chữ số từ file_name
            match = re.search(r'[A-Za-z0-9]+', filename)
            if match:
                substring = match.group()
                if self.df['Label'].str.contains(substring).any():
                    brix_value = self.df.loc[self.df['Label'].str.contains(
                        substring), 'brix'].values[0]
                    a = brix_value - brix_value * 5 / 100
                    b = brix_value + brix_value * 5 / 100
        except Exception as e:
            logging.error(
                f'Error getting a and b in regression_orange from regression: {str(e)}')
        return a, b
