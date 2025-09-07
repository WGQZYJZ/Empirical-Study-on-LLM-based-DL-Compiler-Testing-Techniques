
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=4)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = v1 * negative_slope
        v3 = torch.where(v1, v2, v1) # Leaky ReLU following a transposed convolution
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
