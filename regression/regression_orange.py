import tensorflow as tf
import logging
from keras.models import load_model

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s|%(name)s|%(levelname)s|%(message)s')

class RegressionModel(object):
    global_model = None

    def __init__(self, model_path, weights_path):
        self.model_path = model_path
        self.weights_path = weights_path
        self.model = self.load_model()
        if self.model is None:
            raise ValueError("Model could not be loaded.")
        # self.model_tflite = self.load_model_tflite()
        # Uncomment the above line if you want to use the tflite model.

    def load_model(self):
        model = None  # Initializing the variable to ensure it is in scope even in case of an exception
        try:
            if RegressionModel.global_model is None:
                with open(self.model_path, 'r') as json_file:
                    model_json = json_file.read()
                model = tf.keras.models.model_from_json(model_json)
                model.load_weights(self.weights_path)
                RegressionModel.global_model = model
            else:
                model = RegressionModel.global_model
        except Exception as e:
            logging.error(f'Error loading model in regression_model from regression: {str(e)}')
            raise  # Re-raising the exception after logging for external handling or notifying the user.

        return model

    def load_model_tflite(self):
        interpreter = None
        try:
            interpreter = tf.lite.Interpreter(model_path=self.weights_path)
            interpreter.allocate_tensors()  # Prepare the interpreter for operation
        except Exception as e:
            logging.error(f'Error loading model tflite in regression_model from regression: {str(e)}')
            raise  # Re-raising the exception might also help in external handling.
        
        return interpreter