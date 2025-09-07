
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        return torch.clamp_max(v2, max_value=5)


# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(4, 8, 64, 32)
 
 __output__  = m(x1)
