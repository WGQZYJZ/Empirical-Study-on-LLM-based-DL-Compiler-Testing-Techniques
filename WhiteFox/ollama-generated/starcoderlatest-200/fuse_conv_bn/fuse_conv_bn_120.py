
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, input_tensor):
        output = bn(self.conv(input_tensor))
        return output


# Inputs to the model
x1 = torch.randn(1, 64, 28, 28)
