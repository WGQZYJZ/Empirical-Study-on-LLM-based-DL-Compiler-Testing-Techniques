
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 4, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1  * 0.5
        v3 = v1 ** 3
        v4 = v3 * 0.044715
        v5 = (v1 + v4) * 0.7978845608028654
        v6 = torch.tanh(v5) + 1
        v7 = v2 * v6
        return v7


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 304, 304)
