
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1) * 0.5
        v2 = ((v1.square() + 1e-5).pow(3)).sqrt()
        v3 = (v2 * v2).cumprod(dim=0)
        v4 = (v2 * v2).cumprod(dim=-1)
        v5 = v4.mul_(0.044715).view(-1) + 1
        v6 = (v1 + v5).sqrt() * 0.7978845608028654
        v7 = torch.tanh(v6).view(-1) + 1
        return v7


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
