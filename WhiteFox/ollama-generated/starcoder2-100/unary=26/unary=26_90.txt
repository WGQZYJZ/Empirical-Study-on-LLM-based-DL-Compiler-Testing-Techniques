
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply transposed convolution to the input tensor
        
        alpha  = -0.5
        v2 = (v1 > 0).float()
        v3 = v1 * alpha
        v4 = torch.where(v2==True, v1, v3 )
        return v4


# Initializing the model
m = Model()

 # Inputs to the model