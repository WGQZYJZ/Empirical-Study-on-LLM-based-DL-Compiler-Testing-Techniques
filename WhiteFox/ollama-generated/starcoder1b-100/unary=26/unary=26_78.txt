
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        mask = (v > 0).float()
        neg_slope = -negative_slope
        mask *= neg_slope
        output = torch.where(mask, x, v)
        return output


# Initializing the model
m = Model(negative_slope=0.1)


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
