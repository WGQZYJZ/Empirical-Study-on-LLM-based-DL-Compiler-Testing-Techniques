
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3  # The addition operator is applied to a constant `3`
        v2 = torch.clamp_min(v1, 0)  # Clamp the output of the addition operation to a minimum of `0`
        v3 = torch.clamp_max(v2, 6)  # Clamp the output of the previous operation to a maximum of `6`
        v4 = v1 * v3  # The clamped and multiplied result is divided by `6`
        return v4


# Initializing the model
m = Model()


