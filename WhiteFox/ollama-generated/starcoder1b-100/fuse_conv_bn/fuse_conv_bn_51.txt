
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...) # X can be 1, 3 or 4 representing the dimension
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        output = self.conv(x)
        return self.bn(output)


# Initializing the model
m = Model()

