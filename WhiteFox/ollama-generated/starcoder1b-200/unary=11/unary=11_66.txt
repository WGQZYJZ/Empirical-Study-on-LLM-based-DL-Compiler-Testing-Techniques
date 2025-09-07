
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 4, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        return v3


# Initializing the model
m = Model()


