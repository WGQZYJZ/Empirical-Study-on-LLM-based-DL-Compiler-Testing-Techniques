
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * torch.exp(v1) + 1j * torch.exp(-v1) # A valid complex number is required to calculate the Hartley transform of the output of the exp function
        v4 = torch.tanh(torch.cat((v2, v3), dim=1))
        v5 = v4 * v2 + 1j * v4 * v3
        v6 = v1 * v5 # The Hartley transform of the output of the multiplication
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 256, 256)
