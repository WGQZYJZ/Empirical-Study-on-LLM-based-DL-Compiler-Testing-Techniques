
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x) + 3
        return torch.clamp_min(v, 0), torch.clamp_max(v, 6) / 6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 128, 128)
