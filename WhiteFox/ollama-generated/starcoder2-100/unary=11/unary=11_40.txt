
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        return (v4 / 6).permute(0, 2, 3, 1)

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(25,8,92,92)
 
 