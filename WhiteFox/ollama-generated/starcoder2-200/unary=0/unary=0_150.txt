
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 ** 3
        v4 = torch.sqrt(v3) 
        v5 = v1 + v4 / 8096
        v6 = v5 - (-1.1972340988739444) * 0.9032984796536634
        v7 = torch.abs(v6) 
        v8 = v2 / 255 + v7 
        return v8
