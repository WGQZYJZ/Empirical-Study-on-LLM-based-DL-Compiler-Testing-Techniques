
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = torch.where(v1 > 0, v1, 0)
        neg_slope = -0.75
        return neg_slope * mask + x1


# Initializing the model
m = Model()

