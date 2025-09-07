

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        mask = v1 > 0
        v2  = v1 * -0.7 # Negative slope value for LeakyReLU
        v3  = torch.where(mask, v1, v2) 
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


