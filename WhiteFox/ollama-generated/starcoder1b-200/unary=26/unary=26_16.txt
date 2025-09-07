
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).type(torch.FloatTensor).to(x1.device) * self.negative_slope
        return torch.where(v2, v1, v3)


# Initializing the model
m = Model()


