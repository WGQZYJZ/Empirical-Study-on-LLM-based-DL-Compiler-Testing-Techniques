
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0) * negative_slope
        v3 = (v1 * negative_slope) + v1  # Use the multiplication result of t1 and negative slope to get the output of the transposed convolution based on mask t2
        return torch.where(t2, v1, v3)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
