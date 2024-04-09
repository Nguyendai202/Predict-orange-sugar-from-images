import os
ROOT_DIR = os.path.dirname(__file__)
MODEL_REGRESSION_CONFIG_PATH = os.path.join(
    ROOT_DIR, "configs/regression-mobilenetv2_0304.json")
MODEL_REGRESSION_WEIGHT_PATH = os.path.join(
    ROOT_DIR, "configs/regression-mobilenetv2-weights_0404.h5")
MODEL_SEGMENT_PATH = os.path.join(ROOT_DIR, 'configs\model_segment')
