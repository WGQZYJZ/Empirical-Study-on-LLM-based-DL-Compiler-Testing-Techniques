
class Model(torch.nn.Module):
    def __init__(self, a=50):
        super().__init__()
        self._a  = a
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2  = torch.cat([v1] * 50, -1) # Concatenation of the result tensor along a specified dimension
 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(300, 64)
x2  = torch.randn(500, 97)
__output__  = m(x1, x2)

