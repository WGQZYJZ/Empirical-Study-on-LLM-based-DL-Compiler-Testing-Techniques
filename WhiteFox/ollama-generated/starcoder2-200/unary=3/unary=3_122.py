
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3_1 = v1 * 0.7071067811865476 # original
        v3_2 = torch.addmm(v2, x1)     # new
        v4_1 = torch.erf(v3_1)
        v4_2 = torch.erf(v3_2)
        v5   = v4_1 + 1
        v6   = v4_2 * v5                # new
        return v6
