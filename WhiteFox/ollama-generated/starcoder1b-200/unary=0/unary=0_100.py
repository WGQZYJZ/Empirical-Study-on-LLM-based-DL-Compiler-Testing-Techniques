
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.tanh(x1 * 0.5)
        v2 = v1 * v1
        v3 = v2 * v1
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return F.tanh(v6 * 0.7978845608028654)


# Initializing the model
m = Model()


