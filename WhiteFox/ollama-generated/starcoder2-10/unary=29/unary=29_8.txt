
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1): 
        v1  = self.deconv(x1)
        v2  = torch.clamp_min(v1, -5)
        v3  = torch.clamp_max(v2, 9876)
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(10, 3, 45, 45)
__output__  = m(x1)

