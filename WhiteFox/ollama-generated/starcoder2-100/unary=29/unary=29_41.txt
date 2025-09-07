
class Model(torch.nn.Module):
    def __init__(self, minval=-256., maxval=256.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose1d(3, 8, kernel_size=7)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, minval)
        v3  = torch.clamp_max(v2, maxval)
        return v3


# Initializing the model
m = Model(-256., -70.)


# Inputs to the model
x1  = torch.randn(1, 8, 96).permute([0, 2, 1]) # Input tensor of the first convolutional layer
__output__   = m(x1)

