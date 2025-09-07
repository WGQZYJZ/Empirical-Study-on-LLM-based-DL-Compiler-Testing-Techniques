
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.conv_transpose2d(x1)
        v2  = torch.tanh(v1) # hyperbolic tangent function
        return v2


# Initializing the model
m  = Model()
__output__  = m(x1)

