
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # clamp_min(x, min) returns the value of the input element for which the minimum value is smaller than `min`
        v4  = torch.clamp_max(v3, 6) 
        v5  = v4 / 6 
        return v5


# Initializing the model
m  = Model() 

# Inputs to the model
x1 = torch.randn(1,8,20,7)
 
# Outputs from the model
