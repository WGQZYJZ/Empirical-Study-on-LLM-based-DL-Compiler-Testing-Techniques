
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=5000) # clamp the output of the transposed convolution to a minimum value with argument `5000`
        v3  = torch.clamp_max(v2, max=98765432) 
        return v3

# Initializing the model