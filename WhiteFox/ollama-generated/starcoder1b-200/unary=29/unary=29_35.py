
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=256) # Clamp the output of the transposed convolution to a minimum value equal to 256
        v3 = torch.clamp_max(v2, max_value=256) # Clamp the output of the previous operation to a maximum value equal to 256
        return v3


# Initializing the model
m = Model()


