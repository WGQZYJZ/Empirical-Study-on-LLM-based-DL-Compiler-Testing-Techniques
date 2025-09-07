
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1) + 3
        v2  = torch.clamp(v1, min=0) 
        v3  = torch.clamp(v2, max=6) 
        v4  = v1 * v3
        return v4 / 6

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 8, 50, 97)
__output__  = m(x1)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2048, 3)
__output__  = m(x1).sum().item()


