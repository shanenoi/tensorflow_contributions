import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
print("========== END OF LOGGING ==========\n")

def block(*args, **kwargs):

    def passingfunction(function):

        def passingargs(*_args, **_kwargs):
            # print(type(kwargs['name']))
            # _kwargs['name_scope'] = tf.name_scope(kwargs['name'])
            return function(*_args, **_kwargs)

        return passingargs

    return passingfunction


@block(name="hello")
@tf.function
def adding(a, b):
        print(a)
        return a + b

    with tf.name_scope("name_scope"):
        a = tf.constant([2, 3])
        b = tf.constant([2, 93])
        c = adding(a, b)
with tf.Session() as ss:
    print(ss.run(c))


