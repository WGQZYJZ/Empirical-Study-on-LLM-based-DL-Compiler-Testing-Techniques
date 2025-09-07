
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = v1 + 3
        v3  = F.clamp(v2, min=0, max=6)
        v4  = torch.div(v3, 6)
        return v4
