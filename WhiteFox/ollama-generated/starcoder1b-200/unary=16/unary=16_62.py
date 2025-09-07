
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, 4, stride=1)
        self.conv2 = torch.nn.Conv2d(6, 8, 4, stride=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return relu(v2)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 80, 80)
