
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Pointwise transposed convolution
        v2 = torch.clamp_min(v1, -5) # Clamp the output of the previous operation to a minimum value
        v3 = torch.clamp_max(v2, 80) # Clamp the output of the previous operation to a maximum value
 
        return v3

m = Model()
x1 = torch.randn(64, 3, 59, 57)
output__ = m(x1)

