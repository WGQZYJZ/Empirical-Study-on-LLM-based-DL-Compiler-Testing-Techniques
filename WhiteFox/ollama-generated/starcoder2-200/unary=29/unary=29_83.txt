
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = torch.clamp_min(v1, -0.9547672990300602) # Clamp the output of the transposed convolution to a minimum value (-0.9547672990300602)
        v3  = torch.clamp_max(v2, -0.918326106436591) # Clamp the output of the previous operation to a maximum value (-0.918326106436591)
        return v3


# Initializing the model and inputs