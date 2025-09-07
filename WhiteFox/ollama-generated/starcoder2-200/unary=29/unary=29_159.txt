
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.clamp_min(v1, min_value=0.5) # Clamp the output of the transposed convolution to a minimum value (0.5)
        return torch.clamp_max(v2, max_value=1.5) # Clamp the output of the previous operation to a maximum value (1.5)

# Initializing the model
m = Model()
__output__  = m(x1)

