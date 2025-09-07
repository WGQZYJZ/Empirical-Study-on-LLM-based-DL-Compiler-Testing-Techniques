
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([3], 1, dtype=torch.int64, layout=torch.Strided, device=x1.device)
        v2 = convert_element_type(v1, torch.float)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
x1 = torch.randn(2, 2, 2)
