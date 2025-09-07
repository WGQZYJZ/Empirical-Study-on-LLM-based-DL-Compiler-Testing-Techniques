
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn = torch.nn.BatchNormXd(...)

    @torch.jit.script_method
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.bn(v1)  # X should match with ConvXd
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(...)  # Permute x1 and feed input_tensor as input to this module
