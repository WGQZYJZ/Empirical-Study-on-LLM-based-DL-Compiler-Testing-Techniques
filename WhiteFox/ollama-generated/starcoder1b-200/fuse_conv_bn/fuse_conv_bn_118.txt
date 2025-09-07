
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    @torch.jit.script_method
    def forward(self, x):
        return self.conv(x).view(-1, self.num_input_channels * self.kernel_size[0] * self.kernel_size[1]).bn(x)


# Inputs to the model
x = torch.randn(1, 2, 2)
