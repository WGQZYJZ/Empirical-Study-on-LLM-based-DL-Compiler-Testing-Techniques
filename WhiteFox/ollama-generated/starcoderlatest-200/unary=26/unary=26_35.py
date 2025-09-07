
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=0)
        self.negative_slope = torch.nn.Parameter(torch.tensor(negative_slope))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
