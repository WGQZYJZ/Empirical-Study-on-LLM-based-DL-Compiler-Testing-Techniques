
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1  = F.sigmoid(v0)
        v2 = v0 * v1
