
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNorm2d(...)
        self.fc = torch.nn.Linear(...)

    def forward(self, x):
        input_tensor  = x.permute(0, 2, 3, 1)
        output = self.bn(self.conv(input_tensor))
        return self.fc(output)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 2, 2)
