import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, threshold=0.0, max_iterations=1000):
        self.weights = np.random.rand(input_size)
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations

    def activate(self, net_input):
        return 1 if net_input >= self.threshold else 0

    def train(self, input_data, labels):
        iteration = 0
        while iteration < self.max_iterations:
            converged = True
            for i in range(len(input_data)):
                input_vector = np.array(input_data[i])
                label = labels[i]
                net_input = np.dot(input_vector, self.weights)
                predicted_output = self.activate(net_input)
                error = label - predicted_output
                if error != 0:
                    converged = False
                    self.weights += self.learning_rate * error * input_vector
            if converged:
                break
            iteration += 1
        return iteration

# Example usage
input_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
labels = [0, 0, 0, 1]

perceptron = Perceptron(input_size=2)
iterations = perceptron.train(input_data, labels)

print("Converged in {} iterations".format(iterations))
print("Final weights:", perceptron.weights)
