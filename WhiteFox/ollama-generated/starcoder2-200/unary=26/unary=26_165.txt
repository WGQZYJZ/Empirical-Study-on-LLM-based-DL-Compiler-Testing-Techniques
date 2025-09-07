
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.2):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose1d(8,3,4)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        
        v1 = self.conv(x1)

        # Apply mask 
        v2  = (v1>0).float() * -1 

        # apply leaky reLU
        v3  = v1 * self.negative_slope

        # Apply where function based on mask and negative slope
        v4 = torch.where((v1 > 0), v3, v2)

        return v4

# Initializing the model with default value for `negative_slope` of 0.2
m = Model(negative_slope=0.2)

 # Inputs to the model
x1  = torch.randn(8,64,5729)
 
 