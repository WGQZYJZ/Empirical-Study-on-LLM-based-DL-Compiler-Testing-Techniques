
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 32, 1)
 
    def forward(self, x2, min_value=0., max_value=255.):
        v2 = self.conv(x2)
        v3 = torch.clamp_min(v2, min_value)
        v4 = torch.clamp_max(v3, max_value)
        return v4


# Initializing the model
m = Model()


