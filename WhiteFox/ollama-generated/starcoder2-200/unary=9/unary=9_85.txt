
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v4 = torch.clamp_max(v0 + 3, 6) / 6 
        return v4
