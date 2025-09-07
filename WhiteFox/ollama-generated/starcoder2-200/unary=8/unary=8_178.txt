
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = v1 + 3 
         v3  = torch.clamp(v2, min=0) # Clamp
         v4  = torch.clamp(v3, max=6) # Clamp
         v5  = v4 / 6 
         return self.deconv(v5)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 28, 28)
__output__  = m(x1).shape