
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1 * v2 # Applying the GLU
        return v3

# Initializing the model with torch.nn.ConvTranspose2d
m = Model()

# Input to the model (of size 64 x 64 x 3)
x1 = torch.randn(1, 3, 64, 64)
