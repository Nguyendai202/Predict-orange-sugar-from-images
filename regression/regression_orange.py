from tensorflow import keras
import tensorflow as tf
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')


class RegressionModel(object):
    global_model = None

    def __init__(self, model_path, weights_path):
        self.model_path = model_path
        self.weights_path = weights_path
        self.model = self.load_model()
        # self.model_tflite = self.load_model_tflite()

    def load_model(self):
        try:
            if RegressionModel.global_model is None:
                # Load model architecture from JSON file
                with open(self.model_path, 'r') as json_file:
                    model_json = json_file.read()
                model = keras.models.model_from_json(model_json)
                # Load model weights from H5 file
                model.load_weights(self.weights_path)
                RegressionModel.global_model = model
            else:
                model = RegressionModel.global_model
        except Exception as e:
            logging.error(
                f'Error loading model in regression_orange from regression: {str(e)}')
        return model

    def load_model_tflite(self):
        try:
            interpreter = tf.lite.Interpreter(model_path=self.weights_path)
        except Exception as e:
            logging.error(
                f'Error loading model tflite in regression_orange from regression: {str(e)}')
        return interpreter
