
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = torch.cat([v1, v2], dim=-1)
        return v3


# Inputs to the model
x  = torch.randn(4, 3, 64, 64)
__output__  = m(x)

