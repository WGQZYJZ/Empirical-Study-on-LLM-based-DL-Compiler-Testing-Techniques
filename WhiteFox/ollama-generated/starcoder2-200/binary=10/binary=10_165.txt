
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor.
        v2  = v1 + other
        return v2


# Initializing the model
m = Model()
other  = torch.tensor([30])
 
# Inputs to the model
x1  = torch.randn(1, 1)
__output__  = m(x1)