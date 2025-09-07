
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.abs(v1) > 0
        negative_slope = -torch.log(1 / (torch.abs(v1) + 1e-6))
        v3 = negative_slope * torch.where(t1, v1, negative_slope)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
