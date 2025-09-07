
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        return torch.clamp_min(v1 + 3, 0), torch.clamp_max(v1 / 6, 6)


# Initializing the model
m = Model()


