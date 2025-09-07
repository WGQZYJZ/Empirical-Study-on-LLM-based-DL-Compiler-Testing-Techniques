
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.deconv(x)
        v2  = v1.clamp(min=0)
        v3  = v2.clamp(max=255)
        return v3

# Initializing the model
m = Model()

