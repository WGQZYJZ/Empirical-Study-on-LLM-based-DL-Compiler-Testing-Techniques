
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)

    @torch.jit._recursive_guard.recursive_guarded
    def forward(self, input):
        return self.bn(self.conv(input))

# Inputs to the model
x1 = torch.randn(2, 3, 2)
