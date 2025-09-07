
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4, x5):
        v1  = self.conv(x1)
        v2  = self.conv(x2)
        v3  = self.conv(x3)
        v4  = self.conv(x4)
        v5  = self.conv(x5)
        v6 = torch.cat([v1, v2], dim=-1)  # Concatenate the two convolution outputs along the -1 dimension
        return v6
 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
x3 = torch.randn(1, 3, 64, 64)
x4 = torch.randn(1, 3, 64, 64)
x5 = torch.randn(1, 3, 64, 64)
