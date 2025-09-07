
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(32, 16, 4)
 
    def forward(self, x):
        v0 = F.upsample_bilinear(x, scale_factor=2) # Applies upsampling to the input tensor using bilinear interpolation
        
        v1 = self.convT(v0)
        return torch.sigmoid(v1)

# Initializing the model
m  = Model()

 # Inputs to the model
 x = torch.randn(3, 8, 64, 64)
 
 __output__  = m(x)