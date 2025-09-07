
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).mul(0.5)
        v2 = (v1 * v1).sqrt()
        v3 = v2 * v1
        v4 = v3 * v1
        v5 = v4.pow_(0.044715)
        v6 = v1 + v5
        v7 = v6.mul(0.7978845608028654)
        v8 = torch.tanh(v7).add_(1)
        v9 = v2 * v8
        return v9


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
