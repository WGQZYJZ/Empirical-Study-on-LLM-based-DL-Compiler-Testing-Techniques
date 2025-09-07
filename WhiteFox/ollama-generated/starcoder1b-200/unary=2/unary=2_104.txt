
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1  + 1
        v4 = v2 * v3
        v5 = torch.tanh(v4)
        v6 = v5 * v5
        return v6


# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
