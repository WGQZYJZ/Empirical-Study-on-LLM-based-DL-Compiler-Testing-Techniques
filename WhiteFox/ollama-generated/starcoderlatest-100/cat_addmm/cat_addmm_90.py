
class Model(torch.nn.Module):
    def __init__(self, channels=128):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, channels, 7)
        self.conv2 = torch.nn.Conv2d(channels, 100, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
