import numpy as np
import matplotlib.pyplot as plt

class CPPN:
    def __init__(self, num_input, num_output, num_hidden_layers=3, 
                 num_hidden_units=32, activation_functions=[np.sin, np.tanh]):
        self.num_input = num_input
        self.num_output = num_output
        self.num_hidden_layers = num_hidden_layers
        self.num_hidden_units = num_hidden_units
        self.activation_functions = activation_functions

        # Initialize weights and biases
        self.weights = []
        self.biases = []
        input_to_hidden = np.random.uniform(low=-1, high=1, size=(self.num_input, self.num_hidden_units))
        self.weights.append(input_to_hidden)
        self.biases.append(np.zeros(self.num_hidden_units))
        
        for _ in range(self.num_hidden_layers - 1):
            hidden_to_hidden = np.random.uniform(low=-1, high=1, size=(self.num_hidden_units, self.num_hidden_units))
            self.weights.append(hidden_to_hidden)
            self.biases.append(np.zeros(self.num_hidden_units))
        
        hidden_to_output = np.random.uniform(low=-1, high=1, size=(self.num_hidden_units, self.num_output))
        self.weights.append(hidden_to_output)
        self.biases.append(np.zeros(self.num_output))

    def activate(self, x):
        for layer in range(len(self.weights)):
            x = np.dot(x, self.weights[layer]) + self.biases[layer]
            activation_func = self.activation_functions[layer % len(self.activation_functions)]
            x = activation_func(x)
        return x

    def compute_image(self, width, height):
        x = np.linspace(-1, 1, width)
        y = np.linspace(-1, 1, height)
        xs, ys = np.meshgrid(x, y)
        rs = np.sqrt(xs**2 + ys**2)
        thetas = np.arctan2(ys, xs)

        inputs = []
        for i in range(self.num_input):
            if i % 4 == 0:
                inputs.append(rs)
            elif i % 4 == 1:
                inputs.append(thetas)
            elif i % 4 == 2:
                inputs.append(np.sin(self.c[i] * rs + self.d[i] * thetas))
            elif i % 4 == 3:
                inputs.append(np.cos(self.c[i] * rs + self.d[i] * thetas))

        inputs = np.array(inputs).transpose()

        # apply the hidden layers
        hiddens = inputs
        for i in range(self.num_hidden_layers):
            hiddens = np.maximum(np.dot(hiddens, self.weights[i]) + self.biases[i], 0)

        # apply the output layer
        rgba = np.dot(hiddens, self.weights[-1]) + self.biases[-1]
        rgba = np.clip(rgba, -1, 1)
        rgba = (rgba + 1) / 2 # scale to 0-1 range
        rgba = (rgba * 255).astype(int) # scale to 0-255 range
        rgba = np.reshape(rgba, (height, width, 4))

        return rgba

# Example usage
cppn = CPPN(num_input=2, num_output=4, num_hidden_layers=8, num_hidden_units=16, activation_functions=[np.cos, np.sin, np.square, np.sin, np.tanh])
image = cppn.compute_image(width=480, height=480)
plt.imshow(image)
plt.show()
