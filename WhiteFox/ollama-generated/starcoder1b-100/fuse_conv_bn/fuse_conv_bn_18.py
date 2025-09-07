
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(...) # ConvNd and BatchNorm2d are used instead of Conv2d and BatchNorm2d. 
        self.bn    = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 8, 8)
