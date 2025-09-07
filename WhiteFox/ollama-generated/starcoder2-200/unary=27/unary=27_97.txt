
class Model(torch.nn.Module):
    def __init__(self, min=1e-3, max=2500):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = torch.clamp_min(v1, min)
         v4  = torch.clamp_max(v2, max)
         return v4

# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
  