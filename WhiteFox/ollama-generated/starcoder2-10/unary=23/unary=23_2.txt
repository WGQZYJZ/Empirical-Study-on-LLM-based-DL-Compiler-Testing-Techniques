
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8,3,1)
 
    def forward(self, x1):
        v0  = (x1)
        v1 = v0 * 0.5
        v2 = v0 + 100
        v4 = self.deconv(v1*v2) 
        return torch.tanh(v4)


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
