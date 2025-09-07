
class Model(torch.nn.Module):
    def __init__(self, min_value=10., max_value=-5.):
        super().__init__()
        self.linear  = torch.nn.Linear(32*8 * 8, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + min_value # Add the minimum value to the output of linear transformation 
        v3  = torch.clamp(v2, -5., max_value) # Clamp the minimum added to the linear transformation result to a maximum value and then clamp the resulting output back to its original value
        return v3


# Initializing the model with keyword arguments: min_value=10.0, max_value=-5.0
m = Model(min_value=10., max_value=-5.)


# Inputs to the model
x1  = torch.randn(4, 32*8 * 8)
__output__  = m(x1)


