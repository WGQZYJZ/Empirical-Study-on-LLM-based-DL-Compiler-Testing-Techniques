
class Model(torch.nn.Module):
    def __init__(self, minval=-2048, maxval=2047):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 15, 1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -2048)
        return torch.clamp_max(v2, 2047)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 650, 900).to(device)

# Model outputs of the model
