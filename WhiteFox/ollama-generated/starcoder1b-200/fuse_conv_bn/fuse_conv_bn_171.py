
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)
        self.bn    = torch.nn.BatchNormXd(...)

    def forward(self, input_tensor):
        conv_output = self.conv(input_tensor)
        bn_output   = self.bn(conv_output)
        return bn_output


# Inputs to the model
x1 = torch.randn(1, 2, 4, 4)
