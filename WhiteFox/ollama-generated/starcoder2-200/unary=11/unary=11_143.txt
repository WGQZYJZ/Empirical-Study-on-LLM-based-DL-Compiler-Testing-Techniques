
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0) #Clamps the output of the addition operation at a minimum of `0`
        v4 = torch.clamp_max(v3, 6) #Clamps the output of the previous operation at a maximum of 6
        v5 = v4 / 6 
        return v5

# Initializing the model