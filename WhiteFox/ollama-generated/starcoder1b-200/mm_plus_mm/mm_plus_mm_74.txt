
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 2, stride=2, padding=2)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return t3


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(2, 8, 64, 64)
