
class Model(torch.nn.Module):
    def __init__(self, min_value: int, max_value: int = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        if max_value:
            v3 = torch.clamp_max(v2, self.max_value)
        else:
            v3 = v2
        return v6

# Initializing the model
m = Model()

