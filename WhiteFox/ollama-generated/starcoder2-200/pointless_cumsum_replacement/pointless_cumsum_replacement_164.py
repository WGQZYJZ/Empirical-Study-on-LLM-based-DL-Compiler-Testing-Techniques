
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1=32):
        v = torch.full([arg1], 1) 
        v  = convert_element_type(v, dtype='torch.int')
        v  = torch.cumsum(v, dim=-1)
        return v


m = Model()

 x1  = torch.randn(1, 32) 
 __output__= m(x1)

# Initializing the model

# Inputs to the model
x1 = torch.randn(1, 64)


