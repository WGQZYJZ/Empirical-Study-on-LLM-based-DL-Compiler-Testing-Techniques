
class Model(torch.nn.Module):
    def __init__(self, use_relu=False):
        super().__init__()

        self.conv = torch.nn.Conv2d(...)
        self.bn = torch.nn.BatchNorm2d(...)

        if not use_relu:
            return 
        
        # TODO: Add the relu layer and apply it to output of convolution layers

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)
        return v2


# Initializing the model with `use_relu` parameter set as True
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 24, 24)
