
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(1024, 100)

    def forward(self, x1):
        x1 = F.relu(self.conv1(x1))

        # 100-dimensional vectors
        z1 = self.fc(x1)

        return z1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 24, 24)
