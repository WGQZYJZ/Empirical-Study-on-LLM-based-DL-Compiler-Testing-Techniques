
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)  # X should match with ConvXd

    def forward(self, x):
        conv_output = self.conv(x)
        bn_output = self.bn(conv_output)
        return bn_output


# Inputs to the model
input_tensor = ...
