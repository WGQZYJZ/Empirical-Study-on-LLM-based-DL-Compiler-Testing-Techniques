
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = (v1 > 0).float()
        v3 = v1 * (-self.negative_slope)
        v4 = torch.where(v2 == True, v1, v3) # This is a typical pattern for a Leaky ReLU operation following a transposed convolution
        return v4

# Initializing the model with negative slope of 0.5
m = Model(negative_slope=0.5)

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
