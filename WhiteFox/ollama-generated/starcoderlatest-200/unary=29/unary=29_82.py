
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1, 3, kernel_size=4)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=9)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
