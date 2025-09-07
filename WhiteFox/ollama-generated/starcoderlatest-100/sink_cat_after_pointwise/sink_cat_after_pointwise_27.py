
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 6, 5)

    def forward(self, x1):
        v1 = torch.cat([x1, x1], dim=1)
        return torch.relu(v1.view(x1.size(0), -1).view(x1.size()))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 32, 32)
