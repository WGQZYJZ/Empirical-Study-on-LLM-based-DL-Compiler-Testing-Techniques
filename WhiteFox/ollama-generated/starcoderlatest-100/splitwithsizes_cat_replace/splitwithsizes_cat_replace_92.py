
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, [16, 32], dim=1)
        v2 = torch.cat([v1[0], v1[1]], dim=1) 
        return v2

# Inputs to the model
x1 = torch.randn(1, 3, 512, 64)
