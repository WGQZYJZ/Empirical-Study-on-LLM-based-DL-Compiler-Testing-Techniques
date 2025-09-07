
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # ConvXd is replaced with Conv2d here.
        self.bn = torch.nn.BatchNorm2d(...)

    def forward(self, x1):
        output = bn(conv(x1)) 
        return output

# Initializing the model
m = Model()


