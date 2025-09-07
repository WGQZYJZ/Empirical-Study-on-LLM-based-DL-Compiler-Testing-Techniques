
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 8, kernel_size=(4, 4), stride=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0 # Apply mask
        v3 = v1 * negative_slope 
        v4 = torch.where(v2, v1, v3) # Apply where function
        return v4

m = Model()


x1 = torch.randn(8, 16, 51, 51)

