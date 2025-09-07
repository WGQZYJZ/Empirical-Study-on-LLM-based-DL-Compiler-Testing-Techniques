
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    @torch.jit.script_method
    def forward(self, input_tensor):
        conv_input_tensor = self.conv(input_tensor)
        output = self.bn(conv_input_tensor)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
