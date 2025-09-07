
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 4)
        self.conv2 = torch.nn.ConvTranspose2d(
            8, 3, kernel_size=(4), stride=2, padding=0
        )

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=-6) # clamp(v2, -inf, 6)
        v4 = torch.clamp(v3, max=0)   # clamp(v3,   0, inf)
        v5 = v1 * v4                    # conv1(x) * clamp(v3,    0,        6)
        v6 = v5 / 6                     # (conv1(x) * clamp(v3, min=0, max=6)) / 6
        return v6

# Initializing the model
m2  = Model()

