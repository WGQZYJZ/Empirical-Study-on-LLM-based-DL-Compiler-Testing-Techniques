
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4) # Apply pointwise transposed convolution to the input tensor
        
    def forward(self, x1):
        v1 = self.conv(x1)
        return_value  = v1 > 0
        mask  = v1 * negative_slope
        
        return torch.where(return_value,v1 ,mask )

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
 
