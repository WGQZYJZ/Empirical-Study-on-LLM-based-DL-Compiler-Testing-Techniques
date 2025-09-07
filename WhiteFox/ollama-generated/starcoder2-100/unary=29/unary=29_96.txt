
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=-0.25):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, min=0.1)
        v3 = torch.clamp_max(v2, max=-0.25)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
