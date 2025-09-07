
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convT(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, 0)  
        v4  = torch.clamp_max(v3, 6)   
        v5  = v4 / 6
        return v5


# Initializing the model
m = Model()


