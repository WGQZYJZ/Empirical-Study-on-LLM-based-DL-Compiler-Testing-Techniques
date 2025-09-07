
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 + 3).clamp_(min=0) # Output of the addition is clamped to the min and max of `0` and `6`.
        v3 = torch.clamp_min((v2 / 6), 6) # Output of the division is clamped to the `6` maximum.
        return v3


# Initializing the model
m = Model()


