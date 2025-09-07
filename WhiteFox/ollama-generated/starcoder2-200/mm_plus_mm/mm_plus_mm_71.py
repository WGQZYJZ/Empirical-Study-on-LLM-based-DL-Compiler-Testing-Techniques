
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.functional.linear # Linear function, that has a 5x3 input layer and 6 output layers
        self.mm2 = torch.nn.Linear # Fully connected neural network that takes 784 inputs and has 100 hidden layers, each of which contains 10 output units 
        self.relu  = torch.nn.ReLU()
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = torch.mm(x, y)
        v2 = self.mm1(v1).view(-1, 6) # Applying the linear function to the matrix multiplication of the inputs and a 5-dimensional tensor. Since 5x3 is mapped to 6 in the 6th dimension. Hence flattened, using -1, we get an output that matches the 5x784x3 size.
        v3 = self.mm2(v2) # Applying the fully connected neural network to the matrix multiplication of the 5-dimensional tensor and a 784-dimensional tensor with 100 hidden layers each containing 10 output units. 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(2, 5) # Matrix multiplication of 6 dimensions, 784 elements in size. This 1D array corresponds to the inputs that will be multiplied by the 30-dimensional input layer of the linear function.
y = torch.randn(3, 784)

