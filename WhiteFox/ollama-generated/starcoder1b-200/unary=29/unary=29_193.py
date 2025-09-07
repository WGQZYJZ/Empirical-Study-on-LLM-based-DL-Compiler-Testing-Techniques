
class Model(torch.nn.Module):
    def __init__(self, max_value=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.clamp_min = lambda x: x - max_value
        self.clamp_max = lambda x: x + max_value
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=0)
        return v3


# Initializing the model
m = Model()

