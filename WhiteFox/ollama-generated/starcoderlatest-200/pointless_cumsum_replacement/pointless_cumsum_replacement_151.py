
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([2, 3], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
