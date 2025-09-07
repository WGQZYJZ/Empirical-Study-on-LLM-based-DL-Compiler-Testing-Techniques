
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=1.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()
