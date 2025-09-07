
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...) # X can be 1, 3 or 4 representing the number of input channels and the channel sizes respectively.
        self.bn1   = torch.nn.BatchNorm2d(...)
        self.relu  = torch.nn.ReLU(...)
        self.conv2 = torch.nn.Conv2d(...) # X can be 1, 3 or 4 representing the number of output channels and the channel sizes respectively.
        self.bn2   = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        x  = self.relu(self.bn1(self.conv1(x)))
        x  = self.conv2(x)
        return self.bn2(x)

# Initializing the model
m = Model()


