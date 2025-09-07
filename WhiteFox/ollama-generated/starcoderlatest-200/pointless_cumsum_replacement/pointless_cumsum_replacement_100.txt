
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], x2.shape[0]], 1, dtype=x1.dtype)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, dim=1)
        return v3
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64).long()
x2 = torch.ones_like(x1)
