
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.bn1 = torch.nn.BatchNorm2d(8)
 
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
        self.bn2 = torch.nn.BatchNorm2d(16)
 
    def forward(self, x1):
        x2 = self.conv1(x1) + 1e-7
        x2 = self.bn1(x2)
        x3 = self.conv2(x2) + 1e-7
        x3 = self.bn2(x3)
        v1 = torch.tanh(x3)
        return v1


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
