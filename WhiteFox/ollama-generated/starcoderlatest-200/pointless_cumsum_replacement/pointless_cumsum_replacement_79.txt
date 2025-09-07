
class Model(torch.nn.Module):
    def __init__(self, shape, dtype=torch.float32):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = convert_element_type(torch.full([shape[0], shape[1]], 1, dtype=dtype), dtype)
        v2 = self.conv(x1)
        v3 = torch.cumsum(v2, 1)
        return v3


# Inputs to the model
shape = (4, 4)
x1 = torch.randn(*shape)
