
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(3, 8, 4) # Transposed convolution with kernel size 4 and output channels 8
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0 
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model with negative slope of `negative_slope`
m = Model()

 # Inputs to the model (note that the input has the same shape as the input from the previous example, and the negative_slope parameter is not used in this example.)
x1  = torch.randn(1024, 3)
__output__  = m(x1)
