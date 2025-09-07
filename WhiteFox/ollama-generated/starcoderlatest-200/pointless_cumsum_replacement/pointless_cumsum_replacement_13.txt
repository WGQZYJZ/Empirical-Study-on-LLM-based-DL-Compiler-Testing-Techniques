
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg2, arg3):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v6

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
arg2 = x1.shape[1]
arg3 = x1.shape[2]
