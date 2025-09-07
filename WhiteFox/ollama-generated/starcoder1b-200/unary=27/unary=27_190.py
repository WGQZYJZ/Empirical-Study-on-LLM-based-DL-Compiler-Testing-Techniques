
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        clamp_max = torch.clamp_max(v1, max_value)
        clamp_min = torch.clamp_min(v2, min_value)
        return clamp_max + clamp_min


# Initializing the model
m = Model()


