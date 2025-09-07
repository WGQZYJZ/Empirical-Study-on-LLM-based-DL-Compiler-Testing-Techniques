
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min(-0.5)) # Clamp to a minimum value of -0.5
        v3  = torch.clamp_max(v2, max(+0.78947368421)) # Clamp to a maximum value of +0.78947368421
        return v3


# Initializing the model