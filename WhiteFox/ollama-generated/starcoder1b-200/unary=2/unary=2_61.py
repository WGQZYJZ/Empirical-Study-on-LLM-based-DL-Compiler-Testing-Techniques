
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3
        v4 = v3 * 0.044715
        v5 = (v1 + v4)
        v6 = (v2 * v5).tanh()
        v7 = (v6 + 1)
        return v7


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
