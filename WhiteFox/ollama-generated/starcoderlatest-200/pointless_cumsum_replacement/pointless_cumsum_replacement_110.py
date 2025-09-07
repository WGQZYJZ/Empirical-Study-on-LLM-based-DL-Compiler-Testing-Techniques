
class Model(torch.nn.Module):
    def __init__(self, dtype=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([x1.size()[0], 1, x1.size()[2], x1.size()[3]], 1, dtype=dtype)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, dim=1)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
