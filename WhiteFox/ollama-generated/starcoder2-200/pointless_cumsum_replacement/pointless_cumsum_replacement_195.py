
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([256, 4], 1)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = convert_element_type(self.t1, x.dtype)
        v2 = torch.cumsum(v1, 1)

        # The inputs to the model:
        v3 = self.conv(x)
        return torch.cat([v2, v3], dim=0)


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
