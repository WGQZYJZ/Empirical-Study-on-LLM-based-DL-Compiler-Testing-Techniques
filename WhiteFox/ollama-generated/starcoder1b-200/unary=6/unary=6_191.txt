
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1 + 3, 0) # v2 will be clamped to 0 - 6
        v3 = torch.clamp_max(v2, 6) # v3 will be clamped to 7 - 5
        v4 = (v1 * v3) / 6 # The result of the division is clamped back to the range [0, 6]
        return v4


# Initializing the model
m = Model()


