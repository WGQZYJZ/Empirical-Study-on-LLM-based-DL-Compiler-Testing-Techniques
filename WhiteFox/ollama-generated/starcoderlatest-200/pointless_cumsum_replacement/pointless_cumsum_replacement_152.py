
class Model(torch.nn.Module):
    def __init__(self, arg1, arg2):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([arg1, arg2], 1, dtype=x1.dtype)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3

# Initializing the model
m = Model(3, 64)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = x1.dtype
