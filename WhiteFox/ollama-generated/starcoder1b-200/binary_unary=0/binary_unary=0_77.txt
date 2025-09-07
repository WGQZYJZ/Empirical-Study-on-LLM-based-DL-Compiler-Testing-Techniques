
class Model(torch.nn.Module):
    def __init__(self, x2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = x2
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other
        return torch.relu(v1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
