
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], 3], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2 = convert_element_type(v1, x2.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
__inputs__ = [torch.randn(1, 3, 64, 64), "float32"]
