 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # Note: input is 4D, so it has a different output channel for each feature map

        self.bn1 = torch.nn.BatchNorm2d(...)
        self.bn2 = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        v1 = self.conv(x) # conv requires the input to be 4D
        v2 = self.bn1(v1)
        v3 = self.bn2(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 2, 2) # Note: batch size is set to 1 since Conv2d only supports batch norm with batch size of 1
