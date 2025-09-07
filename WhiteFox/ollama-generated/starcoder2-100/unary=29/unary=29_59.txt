
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=10):
        super().__init__()
 
        self.min = float(min_value) if min_value is not None else 0
        self.max = float(max_value)
 
        self.conv  = torch.nn.ConvTranspose2d(32, 8, 7, stride=1, padding=3)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=self.min)
        v3  = torch.clamp_max(v2, max=self.max)
        return v3


# Initializing the model with min and max values specified