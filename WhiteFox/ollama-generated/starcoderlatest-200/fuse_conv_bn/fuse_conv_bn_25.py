
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 2, (1, 2))

    def forward(self, x):
        return self.bn(self.conv(x))

    def bn(self, input):
        return torch.nn.functional.batch_norm(input)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
