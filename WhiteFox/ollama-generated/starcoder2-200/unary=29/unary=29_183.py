
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, min(-1)) # clamp output of the conv to a minimum value 
        v3 = torch.clamp_max(v2, max(-0.5))  # clamp output of previous operation to a maximum value
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

