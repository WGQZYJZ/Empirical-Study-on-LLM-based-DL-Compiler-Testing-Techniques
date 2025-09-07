
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1).div(0.5)
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2).add_(1.0)
        v4 = (x2 @ v2.unsqueeze(-1)).mul_(0.5)
        v5 = v4 * x1
        v6 = (v5.mul_((1.0-dropout_p)**2)).sum(dim=1, keepdim=True).sub_(1.0)
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 15, 15)
