
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.full([10, 4], 1, dtype=x1.dtype)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, dim=x1.ndim - 1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5, dtype=torch.int64)
