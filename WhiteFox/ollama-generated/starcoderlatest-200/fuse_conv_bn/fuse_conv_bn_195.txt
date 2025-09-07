
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 5)

    def forward(self, x):
        y = x.permute(0, 2, 3, 1)
        z = self.conv1(y)
        return z


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 4, 5)
