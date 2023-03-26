import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as im
import random

def tanh(x):
    return np.tanh(x)

def cos(x): 
    return np.cos(x)

def relu(x):
    return x > 0 # 1 if true 0 otherwise

class Layer:
    def __init__(self) -> None:
        self.input = None
        self.output = None

    def forward_propagation(self):
        NotImplementedError

    def backward_propagation(self):
        NotImplementedError

class FCLayer(Layer):
    def __init__(self, input_size, output_size) -> None:
        super().__init__()
        self.weights = np.random.rand(input_size, output_size) - 0.5
        self.bias = np.random.rand(1, output_size) - 0.5

    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

class RGBLayer(FCLayer):
    def __init__(self, input_size, output_size, rgb_coeffs, rgb_offset) -> None:
        super().__init__(input_size, output_size)
        self.rgb_coeffs = rgb_coeffs
        self.rgb_offset = rgb_offset

    def output_to_rgb(self):
        for i in range(len(self.input_size)):
            for j in range(3):  # RBB values
                accumulator = 0
                for k in range(len(self.output_size)):
                    accumulator += self.input[i][k]*self.weights[j][k]
                self.output.push(
                    math.floor((math.sin(accumulator)/2+0.5)*self.rgb_coeffs[j]+self.rgb_offset[j]))
            self.output.push(255) 

class ActivationLayer(Layer):
    def __init__(self, activation) -> None:
        super().__init__()
        self.activation = activation

    def forward_propagation(self, input_data):
        self.input = input_data
        return self.activation(self.input)

class Network:
    def __init__(self) -> None:
        self.layers = []

    def add(self, layer: Layer):
        self.layers.append(layer)

    def predict(self, input_data):
        samples = len(input_data)
        result = []

        for i in range(samples):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
                result.append(output)
        return result

x_train = [[0] * 480] * 480
for i in range(len(x_train)):
    for j in range(len(x_train)):
        x_train[i][j] = random.randint(0, 255)

x_train = np.array(x_train)

nn = Network()
nn.add(FCLayer(len(x_train), 20))
for i in range(7):
    nn.add(FCLayer(20, 20))
    nn.add(ActivationLayer(tanh))
    nn.add(FCLayer(20, 20))
    nn.add(ActivationLayer(cos))
nn.add(FCLayer(20, 3))
nn.add(ActivationLayer(tanh))
out = nn.predict(x_train)

out_to_rgb = []

for i in range(len(out)):
    for j in range(len(out[i])):
        for k in range(len(out[j])):
            out_to_rgb.append(out[i][j][k] )

rgb_data = np.arange(0, len(out_to_rgb), 1, np.uint0)
rgb_data = np.resize(rgb_data, (480, 480))
print(rgb_data.shape)
print(rgb_data)

# final_img = im.fromarray(rgb_data)
# final_img.save('img.png')

plt.imshow(rgb_data)
plt.show()
