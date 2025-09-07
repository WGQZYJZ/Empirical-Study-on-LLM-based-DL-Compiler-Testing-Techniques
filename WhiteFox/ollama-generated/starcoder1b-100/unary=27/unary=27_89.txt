
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=None, max_value=None):
        if not isinstance(min_value, (float, int)) or min_value < 0 or not isinstance(max_value, (float, int)) or max_value <= min_value:
            raise ValueError('Invalid arguments for min_value/max_value')
 
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

