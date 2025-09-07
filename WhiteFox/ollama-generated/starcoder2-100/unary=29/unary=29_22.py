
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = torch.clamp_min(v1, -0.5)
        return torch.clamp_max(v2, 0.5)

# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(1, 8, 3, 4)

