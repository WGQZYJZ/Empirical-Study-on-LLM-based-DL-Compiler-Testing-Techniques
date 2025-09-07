
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg0, arg1):
        v0 = torch.full([arg0, arg1], 1, dtype=torch.double)
        v1 = convert_element_type(v0, dtype=torch.float64)
        return torch.cumsum(v1, dim=1)


# Inputs to the model
__input__ = torch.randn(5, 8)
x0 = __input__[0]
x1 = __input__[1]
y0 = m(x0, x1)

