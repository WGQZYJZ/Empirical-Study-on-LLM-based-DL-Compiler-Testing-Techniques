
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * 1e-5 + v1
        v3 = v2 * self.negative_slope
        return torch.where((v1>0).float(), v2, v3)


m  = Model(-1.)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
