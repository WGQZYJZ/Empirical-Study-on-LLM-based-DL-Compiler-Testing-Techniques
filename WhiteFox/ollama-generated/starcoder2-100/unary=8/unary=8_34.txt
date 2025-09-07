
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
    
    def forward(self, x):
        v0  = self.conv(x).type(torch.double)
        v1  = v0 + 3
        v2  = torch.clamp(v1,min=0)
        v3  = torch.clamp(v2,max=6)
        v4  = v0 * v3 
        v5  = v4 / 6 
        return v5

# Initializing the model
m = Model() 

# Inputs to the model
x1 = torch.randn(1, 3, 3, 3).type(torch.float) # For a sample, we generate a random 3D tensor with 3 channels and size [3, 3, 3]
