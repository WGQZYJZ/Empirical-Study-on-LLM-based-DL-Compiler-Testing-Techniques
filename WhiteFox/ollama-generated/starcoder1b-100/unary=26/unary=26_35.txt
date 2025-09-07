
class Model(nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv  = nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = torch.where(v1 > 0, v1, self.negative_slope * x1)
        return v1 + mask


# Initializing the model
m = Model()


