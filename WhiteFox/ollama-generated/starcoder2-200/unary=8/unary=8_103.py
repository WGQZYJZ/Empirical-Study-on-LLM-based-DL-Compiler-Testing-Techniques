
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1): 
        v0 = self.conv(x1) # Transposed convolution
        v1 = v0 + 3 # Add 3 to the transposed convolution output
        v2 = torch.clamp(v1, min=0, max=6) # Clamp the addition output
        v4 = v2 / 6 
        return v4

m  = Model()
