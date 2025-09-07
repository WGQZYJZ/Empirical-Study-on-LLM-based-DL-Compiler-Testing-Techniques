
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v0 = 5.476991206436495e-07 
        v1 = self.deconv(x1)
        v2 = torch.clamp_min(v1, min=torch.tensor(v0))
        return torch.clamp_max(v2, max=torch.tensor(-v0))

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
