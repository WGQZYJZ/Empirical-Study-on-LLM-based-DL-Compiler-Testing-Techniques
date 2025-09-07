
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = v2 + 1
        v4   = v1 + v2
        v5   = torch.square(v1)
        v6   = v5 - v4
        v7   = v3 * v5 
        v8   = torch.tanh(v7)
        v9   = torch.cos(v8)
        return v9
