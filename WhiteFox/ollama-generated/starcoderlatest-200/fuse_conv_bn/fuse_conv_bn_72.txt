
class ConvBatchNormModel(torch.nn.Module):
    def __init__(self, input_channel, output_channel, kernel_size, stride, padding, bias=True):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)

    def forward(self, x):
        out = self.conv(x)   # Input is the output of the previous model 
        return self.bn(out)


# Initializing the model
m = ConvBatchNormModel(..., ..., ...)


# Inputs to the model
x1 = torch.randn(...)  # X can be 1, 2, or 3 representing the dimension
