
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=2)
        self.conv2 = torch.nn.Conv2d(8, 4, 5, stride=2)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
