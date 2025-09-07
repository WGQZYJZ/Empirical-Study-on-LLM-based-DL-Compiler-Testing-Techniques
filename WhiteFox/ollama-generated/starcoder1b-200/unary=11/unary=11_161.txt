
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 1)
 
    def forward(self, x2):
        v2 = self.conv(x2) + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        return v4 / 6


# Initializing the model
m = Model()


