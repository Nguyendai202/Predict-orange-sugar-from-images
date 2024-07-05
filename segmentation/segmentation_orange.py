import cv2
import numpy as np
import tensorflow as tf
import cv2
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')


class CamSegmentationModel(object):
    global_model = None

    def __init__(self, model_path):
        self.model_path = model_path
        # self.weights_path = weights_path
        self.model = self.load_model()

    def load_model(self):
        try:
            if CamSegmentationModel.global_model is None:
                model = tf.saved_model.load(self.model_path)
                CamSegmentationModel.global_model = model
        except Exception as e:
            logging.error(
                f'Error loading model in segmentation_orange from segmentation: {str(e)}')
        return model

    def image_segment(self, image):
        try:
            img_old = cv2.resize(image, (256, 256))
            # img_old = cv2.cvtColor(img_old, cv2.COLOR_BGR2RGB)
            img = np.array(img_old, dtype=np.float64)
            imgnormal = img * 1 / 255.0
            image = np.expand_dims(imgnormal, axis=0).astype(np.float32)
            predict = self.model(image)
            mask = np.round(predict[0])
            mask = tf.cast(mask, dtype=tf.uint8)*255
            if img_old.shape[:2] != mask.shape[:2]:
                mask = cv2.resize(
                    mask, (img_old.shape[1], img_old.shape[0]))
            # Chuyển đổi mask thành float32
            mask = tf.cast(mask, dtype=tf.float32) / \
                255.0  # chuyển về dạng 0-1
            # element wise từng kênh màu với mask
            result = np.multiply(img_old, mask)
        except Exception as e:
            logging.error(
                f'Error segmenting image in segmentation_orange from segmentation: {str(e)}')
            result = img_old
        return result
