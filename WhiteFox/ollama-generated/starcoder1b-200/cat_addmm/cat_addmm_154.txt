
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        v = torch.addmm(x, self.fc1.weight, self.fc1.bias) # Perform a matrix multiplication of weight and bias and add it to the input tensor
        return v


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(2, 32, requires_grad=True)  # Randomly initializes the model inputs
w  = torch.randn(10, 10, 10) * 1.1  # Initializes the weights
b  = torch.zeros(10)  # Initializes the bias
