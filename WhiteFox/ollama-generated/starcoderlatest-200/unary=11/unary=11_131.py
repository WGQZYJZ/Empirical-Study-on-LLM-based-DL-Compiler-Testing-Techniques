
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, 0, 6)
        v4 = v3 / 6
        return v4


# Input to the model
x1 = torch.randn(1, 8, 64, 64)
