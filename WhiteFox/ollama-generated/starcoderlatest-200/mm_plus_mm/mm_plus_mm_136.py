
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 10)
        self.conv2 = torch.nn.Conv2d(64, 32, 7)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Inputs to the model
x1 = torch.randn(10, 64, 56, 56)
x2 = torch.randn(8, 32, 7, 7)
