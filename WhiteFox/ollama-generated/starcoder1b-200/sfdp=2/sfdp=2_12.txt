
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.cat([v1, self.conv2(v1)], dim=1)
        return v2


# Inputs to the model
x = torch.randn(3, 8, 64, 64)
