
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.convt = torch.nn.ConvTranspose2d(
            8, 8, 1, stride=1, padding=1, output_padding=0, groups=1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0, max=6)
        v4  = v3 / 6
