
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4)
        self.clamp_min = torch.nn.ReLU(inplace=True)
        self.clamp_max = torch.nn.Hardtanh(0, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.clamp_min(v1)
        v3 = self.clamp_max(v2)
        return v3


# Initializing the model
m = Model(min_value=0, max_value=1)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
