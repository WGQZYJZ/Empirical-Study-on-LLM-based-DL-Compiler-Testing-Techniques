
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale = torch.nn.Parameter(torch.ones((1, 4)))
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * self.scale
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (v2 * v5).sum(-1, keepdim=True)
        return v6


# Initializing the model
m  = Model()
m.scale.data.normal_(0, 0.01)
