
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(32, 64) * 5 + 2  # Initialize a tensor with random values and scale it by the constant 5, then add the constant 2 to the output of the random tensor.
        v1  = torch.relu(v0)    # Apply the ReLU (Rectified Linear Unit) activation function to the output of the random tensor
        return v1
 
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 64) * 5 + 2
__output__  = m(x1)

