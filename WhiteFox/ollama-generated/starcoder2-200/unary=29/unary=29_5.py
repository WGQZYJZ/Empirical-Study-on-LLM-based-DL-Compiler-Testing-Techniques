
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = torch.clamp_min(v1, min=10) 
        return torch.clamp_max(v2, max=-5) 

# Initializing the model 
m = Model()

 # Inputs to the model 
x1 = torch.randn(8, 3, 64, 64) 

 