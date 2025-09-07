
class Model(nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = torch.where(v1 > 0, x1, torch.zeros_like(x1))
        negative_slope = self.negative_slope * (2 / float(float(mask.size()[2]) * float(mask.size()[3])))
        return torch.abs_(v1) * negative_slope


# Initializing the model
m = Model()


