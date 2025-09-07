
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 + self.conv2(x)
        return v2


# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(3, 8, 1, stride=1, padding=1)
