
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        return torch.clamp(v1, min=0, max=6) / 6


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(2, 8, 128, 128)
