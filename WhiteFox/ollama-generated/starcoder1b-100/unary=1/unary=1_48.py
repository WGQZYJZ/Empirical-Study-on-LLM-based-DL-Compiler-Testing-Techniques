
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear  = torch.nn.Linear(4096, 100)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = (v1 + ((v1 * v1) * 0.044715)) * 0.7978845608028654
        v4 = torch.tanh(v3)
        v5 = v2 * v4
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 256, 256)
