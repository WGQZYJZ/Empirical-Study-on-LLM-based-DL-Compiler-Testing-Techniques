
class Model(torch.nn.Module):
    def __init__(self, max=437918020, min=-563008577):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, min)
        v3 = torch.clamp_max(v2, max)
        return v3


# Initializing the model with provided min and max values for clamping: 
m = Model(max=437918020, min=-563008577)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
