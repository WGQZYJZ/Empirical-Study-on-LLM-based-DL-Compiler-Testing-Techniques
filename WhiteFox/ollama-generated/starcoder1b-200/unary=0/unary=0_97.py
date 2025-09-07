
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = (v1 ** 2).view(-1) * 0.044715
        v4 = (v3 ** 2).view(-1)
        v5 = v4 * 0.7978845608028654
        v6 = torch.tanh(v5) + 1
        v7 = v2 * v6
        return v7


# Initializing the model
m = Model()
__input__ = torch.randn(1, 3, 64, 64)
