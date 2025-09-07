
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return sigmoid(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 8, 64, 64)
