
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    @torch.jit.export
    def forward(self, x):
        out = self.conv(x)
        return self.bn(out)


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
