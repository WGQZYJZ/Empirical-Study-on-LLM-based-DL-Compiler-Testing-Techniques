
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = torch.where(v2, torch.full((v2.shape), self.negative_slope), v1)
        return v3


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
