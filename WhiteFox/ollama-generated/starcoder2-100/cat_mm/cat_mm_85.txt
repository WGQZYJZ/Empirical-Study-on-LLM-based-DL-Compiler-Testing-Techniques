

class Model(torch.nn.Module):
    def __init__(self, num=10):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * num, -1)  # Concatenation of the result tensor along a specified dimension
        return v2


# Initializing model
m = Model()
 
# Inputs to the model
x1 = torch.randn(50, 368493)
x2 = torch.randn(72, 368493)
__output__  = m(x1, x2)

