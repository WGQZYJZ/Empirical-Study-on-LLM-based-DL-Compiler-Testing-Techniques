
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        v2 = v1.clamp_(min=0).clamp_(max=6)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6) / 6
        return v4


# Initializing the model
m = Model()

