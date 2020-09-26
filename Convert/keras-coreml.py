import coremltools as ct
import tensorflow as tf

# Use coremltools to convert a keras model to a mlmodel

tf_keras_model = tf.keras.models.load_model("yolov3.h5")
coreml_model = ct.convert(tf_keras_model,
                          inputs=[ct.ImageType(scale=1/255.0)])

coreml_model.save('Yolov3.mlmodel')
