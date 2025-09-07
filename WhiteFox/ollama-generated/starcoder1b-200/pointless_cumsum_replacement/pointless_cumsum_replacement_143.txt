
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v3 = convert_element_type(v2, dtype)
        return torch.cumsum(v3, 1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
