
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        k = torch.randn(1, 4, 7, 7)
        v = torch.randn(1, 4, 7, 7)
        x2 = self.conv(x1)
        x3 = (x2 * 0.5).add_(v.mul(0.5))
        x4 = ((torch.erf((x3.mul(0.7071067811865476)).mul_(0.7071067811865476))).add_(1).mul(0.9238795325112867)
        x5 = (x2 * x4).mul(0.3)
        return x5

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
