
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value) # <|end_of_code|>
        return torch.clamp_max(v2, max_value)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
