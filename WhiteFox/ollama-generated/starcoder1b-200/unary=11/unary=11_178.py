
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x):
        v = self.conv(x) + 3
        v = torch.clamp_min(v, 0)
        v = torch.clamp_max(v, 6)
        v /= 6
        return v

# Initializing the model
m = Model()

