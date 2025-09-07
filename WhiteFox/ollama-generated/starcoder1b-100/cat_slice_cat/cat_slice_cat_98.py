
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.cat([v1[:,0:9223372036854775807], v1[0:size]], dim=1)
        v3 = torch.cat([v2[0:size, :]], dim=1)
        v4 = torch.cat([v2[0:size, 0:9223372036854775807], v2[9223372036854775807:]], dim=1)
        return v4
