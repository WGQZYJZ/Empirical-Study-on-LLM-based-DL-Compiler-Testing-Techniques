
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        v1 = torch.full([549], 1, dtype=float) 
        v2 = convert_element_type(v1, float32)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x0 = torch.randn(549,)


__output__  = m(x0)
