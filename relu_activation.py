# === Activation ===
from tensorflow.keras.layers import Layer
from tensorflow.keras import backend as K
from keras.utils import get_custom_objects


class ReLU(Layer):
    """
    Rectified Linear Unit.

    It allows a small gradient when the unit is not active:
        f(x) = alpha * x for x < 0
        f(x) = x for x >= 0

    """

    def __init__(self, alpha=0.0, max_value=None, **kwargs):
        super(ReLU, self).__init__(**kwargs)
        self.supports_masking = True
        self.alpha = alpha
        self.max_value = max_value

    def call(self, inputs):
        return K.relu(inputs, alpha=self.alpha, max_value=self.max_value)

    def get_config(self):
        config = {'alpha': self.alpha, 'max_value': self.max_value}
        base_config = super(ReLU, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

class BiReLU(Layer):
    '''
    BiReLU est une fonction d’activation symétrique autour de zéro

    BiReLU(x) = max(0,x) - max(0, -x)

        Elle est positive pour les grandes valeurs positives
        Négative pour les grandes valeurs négatives
        Nulle autour de zéro (contrairement à ReLU qui est nulle à gauche uniquement)
    
    '''
    def __init__(self, alpha=0.0, max_value=None, **kwargs):
        super(BiReLU, self).__init__(**kwargs)
        self.supports_masking = True
        self.alpha = alpha
        self.max_value = max_value

    def call(self, inputs):
        return K.relu(inputs, alpha=self.alpha, max_value=self.max_value) \
               - K.relu(-inputs, alpha=self.alpha, max_value=self.max_value)

    def get_config(self):
        config = {'alpha': self.alpha, 'max_value': self.max_value}
        base_config = super(BiReLU, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))


get_custom_objects().update({'ReLU': ReLU})
get_custom_objects().update({'BiReLU': BiReLU})