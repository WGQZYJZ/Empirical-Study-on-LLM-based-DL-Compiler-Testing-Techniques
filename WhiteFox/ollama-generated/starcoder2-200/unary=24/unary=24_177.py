
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() * -0.5
        v3  = v1 + torch.clamp(-0.7071067811865476, max=0.)
        return torch.where(v2 == 0., v3, v1)
