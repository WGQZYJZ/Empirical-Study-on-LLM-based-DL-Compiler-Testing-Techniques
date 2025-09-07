
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(2)
        v2 = torch.cat([v1, v1], dim=-1)
        v3 = v2.sum(-1)
        v4 = torch.cat([v2.sum(-2), v2.sum(-2)], dim=0)
        v5 = (v4 * 0.044715).pow(1/2)
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        return v8


# Initializing the model
m = Model()


