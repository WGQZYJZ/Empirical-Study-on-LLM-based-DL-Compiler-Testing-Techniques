
class Model(torch.nn.Module):
    def __init__(self, min_value=-3, max_value=5.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 8, 3, stride=1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

# Initializing the model
m  = Model(-7,-5)

 # Inputs to the model
x1=torch.randn(1, 64, 80, 90)
 
 