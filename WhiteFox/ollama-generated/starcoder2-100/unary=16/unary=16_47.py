
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(8, 3, 64, 64).permute((0, 3, 2, 1)) # permute the dimensions of a tensor in order to reshape it as a 5D tensor instead of a 4D tensor.
__output__  = m(x1)

