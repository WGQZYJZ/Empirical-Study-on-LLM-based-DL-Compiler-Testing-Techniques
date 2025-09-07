
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-3, max_value=0.9999):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        clamp_min = torch.clamp_min(v1, min_value)
        clamp_max = torch.clamp_max(clamp_min, max_value)
        return clamp_max


# Initializing the model
m  = Model(0.5, 1.)

