
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.convT  = torch.nn.ConvTranspose2d(8, 3, 4, stride=2)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, -10.)
        v3  = torch.clamp_max(v2, +10.)
        return self.convT(v3)


# Initializing the model