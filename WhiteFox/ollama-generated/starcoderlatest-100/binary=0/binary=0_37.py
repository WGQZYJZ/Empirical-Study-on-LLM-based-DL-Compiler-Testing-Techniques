
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        if other is not None:
            self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.other is not None:
            v2 = v1 + self.other
        else:
            v2 = v1  # Should be same as `v1 * 0` to prevent dead code optimization
        return v2


# Initializing the model
m = Model()

