
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = torch.pow(v1, 2)
        v3 = torch.pow(v2, 3)
        v4 = torch.mul(v3, 0.044715)
        v5 = torch.addcdiv(v1, v4, value=1, scale=0.7978845608028654)
        v6 = torch.tanh(v5) + 1
        return v6


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
