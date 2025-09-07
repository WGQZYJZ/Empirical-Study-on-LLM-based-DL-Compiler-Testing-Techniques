
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=15.0):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, min_value=0.)
        v3  = torch.clamp_max(v2, max_value=15.)
        return v3

# Initializing the model with provided maximum value of clamping operation
m = Model(max_value=4)


