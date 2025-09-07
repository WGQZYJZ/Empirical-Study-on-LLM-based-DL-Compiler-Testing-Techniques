
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.where(v1 > 0, v1 * negative_slope, v1)


# Initializing the model
m = Model()


