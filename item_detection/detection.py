from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import tensorflow as tf

graph = tf.get_default_graph()
def item_detection(img_file):

    # <tensor> is not an element of this graph error に対処
    global graph
    with graph.as_default():

        model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)

        img = image.load_img(img_file, target_size=(224, 224))
        x = image.img_to_array(img)

        # 3次元テンソル（rows, cols, channels) を
        # 4次元テンソル (samples, rows, cols, channels) に変換
        # 入力画像は1枚なのでsamples=1でよい
        x = np.expand_dims(x, axis=0)

        # VGG16の1000クラスはdecode_predictions()で文字列に変換される
        # preprocess_inputでVGG16の平均を引く前処理を行う
        preds = model.predict(preprocess_input(x))
        results = decode_predictions(preds, top=5)[0]

        return results[0][1], results[0][2]