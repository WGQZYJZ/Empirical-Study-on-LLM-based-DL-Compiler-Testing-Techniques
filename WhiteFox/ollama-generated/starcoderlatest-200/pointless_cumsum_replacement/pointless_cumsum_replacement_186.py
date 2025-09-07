
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([100, 20], 1, dtype=torch.float32)
        v2 = convert_element_type(v1, torch.float64)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
x1 = torch.randn(100, 20, dtype=torch.float32)
