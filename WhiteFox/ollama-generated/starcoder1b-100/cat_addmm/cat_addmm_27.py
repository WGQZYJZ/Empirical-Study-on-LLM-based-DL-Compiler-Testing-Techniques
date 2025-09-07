
class Model(torch.nn.Module):
    def __init__(self, width=8):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, width, 1)
        self.conv2 = torch.nn.Conv2d(width, width, 1)
 
    def forward(self, x):
        v = self.conv1(x) * 0.5 + self.conv2(v) * 0.7071067811865476
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 20, 20)
