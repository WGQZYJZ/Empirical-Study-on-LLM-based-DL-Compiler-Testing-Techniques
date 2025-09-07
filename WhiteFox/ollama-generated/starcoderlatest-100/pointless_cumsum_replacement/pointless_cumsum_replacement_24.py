
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], 1, x1.shape[2], x1.shape[3]], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2 = convert_element_type(v1, self.conv.weight.dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
