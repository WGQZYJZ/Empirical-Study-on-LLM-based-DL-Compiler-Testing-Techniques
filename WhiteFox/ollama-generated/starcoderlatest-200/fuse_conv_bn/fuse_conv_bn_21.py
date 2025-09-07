
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(...)

    def forward(self, x1):
        conv_output  = self.conv(x1) # The convolution layer outputs a tensor
        bn_output     = torch.nn.functional.batch_norm(conv_output) # batch normalization function uses the output of the convolution layer as its input
        return bn_output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
