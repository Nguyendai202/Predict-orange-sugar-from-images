import tensorflow as tf

from tensorflow.keras.models import load_model

# Load the .h5 model
model = load_model('configs/regression-mobilenetv2-weights_0404.h5')

# Save the model to the SavedModel format
model.save('regression_model')

# Một thư mục 'path_to_save_pb_model' sẽ được tạo ra,
# chứa định dạng SavedModel bao gồm file .pb và các thư mục assets và variables.
