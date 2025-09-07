
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        mask = x1 > 0
        v1 = self.conv(x1[mask])
        neg_slope = 0.05
        slope = 0.5 / (2 * np.pi * negative_slope**2)
        v3 = torch.where(
            mask,
            neg_slope * v1,
            slope * v1
        )
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
