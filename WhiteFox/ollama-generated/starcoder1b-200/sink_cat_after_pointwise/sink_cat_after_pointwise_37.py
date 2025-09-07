
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(2, 4, 3)
        self.conv2 = nn.Conv2d(4, 8, 3)

    def forward(self, x1):
        x1 = self.conv1(x1)
        x2 = self.conv2(x1)
        return x2


# Initializing the model
m = Model()


