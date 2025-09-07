
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
        self.min = min_ # Minimum value to clamp the output of the transposed convolution
        self.max = max_
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = torch.clamp_min(v1, self.min)  # Clamps the output of the previous operation to a minimum value
        v3 = torch.clamp_max(v2, self.max)  # Clamps the output of the previous operation to a maximum value
        return v3


# Initializing the model
m  = Model(-1., -0.)


# Inputs to the model
x1  = torch.randn(4, 8, 56, 56)
