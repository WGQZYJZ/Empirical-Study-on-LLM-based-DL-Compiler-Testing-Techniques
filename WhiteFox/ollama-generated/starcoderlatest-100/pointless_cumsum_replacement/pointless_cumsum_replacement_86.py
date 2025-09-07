
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v = torch.full([3, 64, 64], 1, dtype=x.dtype, layout=x.layout, device=x.device)
        v = convert_element_type(v, x.dtype)
        v = torch.cumsum(v, 1)
        return v


# Inputs to the model
x = torch.randn(2048, dtype=torch.float32)
