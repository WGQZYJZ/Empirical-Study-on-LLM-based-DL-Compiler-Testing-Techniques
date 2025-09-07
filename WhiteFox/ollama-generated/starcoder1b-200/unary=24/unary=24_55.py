
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * self.negative_slope
        v3 = v1 * self.negative_slope  # The second multiply is needed to match the pattern characterized above
        v4 = torch.where(v2 > 0, x1, - v3)  # The where function will apply the multiplications based on the boolean mask created in the previous step
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
