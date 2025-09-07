
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv(x)
        mask = (v1 > 0).type(torch.LongTensor) * -1
        v3 = torch.where(mask, v1, self.negative_slope * v1)
        return v3


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
