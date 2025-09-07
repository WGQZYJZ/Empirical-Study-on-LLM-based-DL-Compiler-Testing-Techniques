
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=None, max_value=None):
        v1 = self.conv(x1)
        if min_value is not None:
            v2 = torch.clamp_min(v1, min_value)
        else:
            v2 = v1
        if max_value is not None:
            v3 = torch.clamp_max(v2, max_value)
        else:
            v3 = v2
        return v3


# Initializing the model
m = Model()


