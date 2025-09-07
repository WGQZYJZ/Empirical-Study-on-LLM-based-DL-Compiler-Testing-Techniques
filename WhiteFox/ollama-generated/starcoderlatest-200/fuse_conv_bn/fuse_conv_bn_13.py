
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 32, (1, 1))
        self.bn    = torch.nn.BatchNorm2d(32)
        self.fc    = torch.nn.Linear(32, 4)

    def forward(self, x):
        x = self.conv1(x) # ConvXd is used instead of conv
        x = self.bn(x)     # BatchNormXd is used instead of bn
        output = self.fc(x)

        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 4, 4)
