
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v1  = self.linear(x1) 
        v2  = v1 + other
        v3  = torch.relu(v2)
        return v3


# Initializing the model with an additional argument for linear transformation
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 8) # The input tensor is passed as positional arguments in the forward method of the module
other  = torch.zeros_like(x1)  # Initialize another input vector with the same shape as the previous one
__output__  = m(x1, other)

