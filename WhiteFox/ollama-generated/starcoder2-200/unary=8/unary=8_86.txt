
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = F.relu6(v2) # clamp_min=0, clamp_max=6
        v4  = v3 * v1 
        v5  = v4 / 6 
        return v5

# Initializing the model
m  = Model()

