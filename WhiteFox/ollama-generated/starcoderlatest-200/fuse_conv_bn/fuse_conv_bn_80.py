
class Model(torch.nn.Module):
    def __init__(self, output_size):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)
        self.bn  = torch.nn.BatchNormXd(...)

    def forward(self, input_tensor):
        conv_output = self.conv(input_tensor)
        batchnorm_output = self.bn(conv_output)
        return batchnorm_output

# Initializing the model
m = Model(2)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
