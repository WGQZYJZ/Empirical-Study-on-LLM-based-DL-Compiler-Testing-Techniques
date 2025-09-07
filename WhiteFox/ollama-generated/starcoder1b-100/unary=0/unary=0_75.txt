
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = v1 ** 2
        v3 = (v1 * 1) ** 3
        v4 = (v2 * v3) ** 0.044715
        v5 = (v1 + v4) ** 0.7978845608028654
        v6 = torch.tanh(v5) + 1
        return v6


# Initializing the model
m = Model()


