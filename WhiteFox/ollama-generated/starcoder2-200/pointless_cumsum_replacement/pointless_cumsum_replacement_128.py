
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v3  = torch.full([arg1, arg2], 1, dtype=dtype) 
        v4  = convert_element_type(v3, dtype) 
        v5  = torch.cumsum(v4, 1) 
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
x2  = torch.randn(arg1, arg2)
__output__   = m(x2)
 
