
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=1e-7)  # clamp the output of the transposed convolution to a minimum value
        v3 = torch.clamp_max(v2, max_value=-1e-7)  # clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8, 160, 256)
