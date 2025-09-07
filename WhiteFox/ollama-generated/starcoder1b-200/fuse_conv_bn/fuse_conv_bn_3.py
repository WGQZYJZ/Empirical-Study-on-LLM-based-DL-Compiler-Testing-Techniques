
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)
        self.bn    = torch.nn.BatchNormXd(...)

    def forward(self, x1):
        # X should match with ConvXd and the shape of `x` should be compatible with the input to conv layer.
        output = self.bn(self.conv(x1))
        return output


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(...)
