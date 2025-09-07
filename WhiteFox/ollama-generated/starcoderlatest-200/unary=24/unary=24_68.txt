
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        negative_slope = -negative_slope
        masked_v1 = torch.where(mask, v1, negative_slope * v1)
        return masked_v1


# Initializing the model and setting its arguments
m = Model(negative_slope=0.3)
