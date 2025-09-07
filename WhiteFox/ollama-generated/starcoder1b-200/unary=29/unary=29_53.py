
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=1 - 1e-5):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=1, padding=1)

    def forward(self, x1, min_value=1e-5, max_value=1 - 1e-5):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
