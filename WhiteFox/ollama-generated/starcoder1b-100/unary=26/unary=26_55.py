
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        m = v1 > 0
        return torch.where(m, v1, -v1 * negative_slope)


# Initializing the model
m = Model()


