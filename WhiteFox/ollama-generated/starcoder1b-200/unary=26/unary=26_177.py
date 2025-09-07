
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, 0, v1 * 0.5)
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
