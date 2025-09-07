
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)

    def forward(self, x):
        output = torch.matmul(x, self.conv1) + self.conv2
        return torch.nn.functional.relu(output)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
