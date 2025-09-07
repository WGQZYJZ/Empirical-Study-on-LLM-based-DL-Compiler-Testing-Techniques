
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value=0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, value=None):
        v1 = self.conv(x1)
        if value is not None:
            t2 = torch.clamp_min(v1, min_value)
            t3 = torch.clamp_max(t2, max_value)
        return v3


# Initializing the model
m  = Model()

