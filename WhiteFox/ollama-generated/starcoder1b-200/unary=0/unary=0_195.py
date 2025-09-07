
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.pow(v1, 0.5)
        v3 = torch.mul(v1, v1)
        v4 = torch.sqrt(v3)
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = torch.tanh(v6)
        v8 = torch.add(v7, 1)
        v9 = torch.mul(v2, v8)
        return v9


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
