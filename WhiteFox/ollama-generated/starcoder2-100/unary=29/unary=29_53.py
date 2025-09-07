
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1.clamp(0.05, 0.95)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
