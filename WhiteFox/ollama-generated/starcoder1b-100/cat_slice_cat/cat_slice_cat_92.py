
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1  = self.conv(x1[:, :96], x2[:, :96])
        v2 = v1  * 0.5
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = t2[:, :9223372036854775807] * t5
        v7 = torch.cat([x1[:, 96:], x2[:, 96:]], dim=1)
        v8 = self.conv(v7[:, :, :-96], v7[:, :, 96:])
        v9 = v8  + 1
        v10 = t3[:, :9223372036854775807] * v9
        return torch.cat([v6, v10], dim=1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
