
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=5) # Replace 5 with a valid minimum value.
        v3 = torch.clamp_max(v2, max=900)# Replace 900 with a valid maximum value.
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1  =  torch.randn(1, 3, 64, 64)
