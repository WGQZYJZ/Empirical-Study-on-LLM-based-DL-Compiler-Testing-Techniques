
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=-50) # Clamp to minimum value -50
        v3 = torch.clamp_max(v2, max=50)# Clamp to maximum value 50
        return v3


# Initializing the model
m  = Model()
