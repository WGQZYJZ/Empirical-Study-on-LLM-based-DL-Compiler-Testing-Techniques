
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = torch.clamp_min(v1, min=-1e-64) # Applying the clamp function with a minimum value of -1e-64
        v3  = torch.clamp_max(v2, max=0.5) # Applying the clamp function with a maximum value of 0.5
        return v3


# Initializing the model
m  = Model()
