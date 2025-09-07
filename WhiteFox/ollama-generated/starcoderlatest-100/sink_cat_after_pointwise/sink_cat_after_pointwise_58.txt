
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(4, 8, kernel_size=3)

    def forward(self, x1):
        x2 = torch.cat([x1, x1, x1], dim=1)
        x3 = torch.relu(x2)
        return self.conv1(x3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 1, 32, 32)
