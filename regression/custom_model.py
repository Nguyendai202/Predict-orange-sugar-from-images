from keras.models import model_from_json
from keras.applications import MobileNetV2
from keras.layers import Input, AveragePooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.models import Model

# Tạo mô hình
input_tensor = Input(shape=(256, 256, 3))
basemodel = MobileNetV2(weights='imagenet', include_top=False, input_tensor=input_tensor)

for layer in basemodel.layers:
    layer.trainable = False

headmodel = basemodel.output
headmodel = AveragePooling2D(pool_size=(4, 4))(headmodel)
headmodel = Flatten(name='flatten')(headmodel)
headmodel = Dense(256, activation="relu")(headmodel)
headmodel = Dropout(0.1)(headmodel)
headmodel = Dense(256, activation="relu")(headmodel)
headmodel = Dropout(0.1)(headmodel)
headmodel = Dense(1, activation='linear')(headmodel)  # Sử dụng activation='linear' cho bài toán hồi quy

model = Model(inputs=basemodel.input, outputs=headmodel)

# Compile mô hình với loss function là mean squared error và optimizer là Adam
model.compile(loss='mean_squared_error', optimizer=Adam(), metrics=["mean_squared_error"])

# Lưu mô hình
model_json = model.to_json()
with open("model_regression.json", "w") as json_file:
    json_file.write(model_json)
