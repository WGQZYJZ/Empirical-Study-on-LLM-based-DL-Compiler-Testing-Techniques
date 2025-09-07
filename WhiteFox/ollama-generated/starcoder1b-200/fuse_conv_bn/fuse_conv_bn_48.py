
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)
        self.bn  = torch.nn.BatchNorm2d(...)

    @torch.jit.script_method
    def forward(self, x1):
        return self.bn(self.conv(x1))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 5) # input should be transposed 1:2:3
