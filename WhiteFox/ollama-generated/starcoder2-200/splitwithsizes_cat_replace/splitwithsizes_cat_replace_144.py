
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, [v for v in range(160)], dim=-1)
        v2 = torch.cat([t for t in v1], -1)
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8, 3, 540, 69)
__output__  = m(x1)

