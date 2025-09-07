
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = (v1 > 0).float() # Apply the mask
        v3  = -5 * v2 + v1 
        v4  = torch.where(v2, v1, v3 ) # Apply where function to choose from output of conv or negative_slope * mask based on mask
        return v4

# Initializing the model
m  = Model()


# Inputs to the model