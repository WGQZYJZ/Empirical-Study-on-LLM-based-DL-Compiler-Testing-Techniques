
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.clamp_min = torch.nn.functional.clamp(min_value, min_value - 0.5, max_value + 0.5)
        self.clamp_max = torch.nn.functional.clamp(max_value, min_value, max_value)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.clamp_min(v1)
        v3 = self.clamp_max(v2)
        return v3


# Initializing the model
m = Model(-2, 2)


