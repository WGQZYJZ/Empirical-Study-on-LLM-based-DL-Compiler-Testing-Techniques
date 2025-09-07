
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)
        self.conv2 = torch.nn.Conv2d(64, 128, kernel_size=5, stride=2, padding=2)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return torch.cat([v1, v2], dim=1)


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
