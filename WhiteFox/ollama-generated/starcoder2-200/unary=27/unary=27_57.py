
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -4) # Clamp the output of the convolution to a minimum value (-4 in this case).
        v3  = torch.clamp_max(v2, 5) # Clamp the result of clamping operation with minimum value to maximum value (5 in this case)
        return v3


# Initializing the model