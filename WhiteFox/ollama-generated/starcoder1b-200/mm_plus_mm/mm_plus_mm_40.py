
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 5)
        self.conv2 = torch.nn.Conv2d(4, 6, 5)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1) * 0.125
        v2 = self.conv2(v1) * 0.5
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 4, 32, 32)
