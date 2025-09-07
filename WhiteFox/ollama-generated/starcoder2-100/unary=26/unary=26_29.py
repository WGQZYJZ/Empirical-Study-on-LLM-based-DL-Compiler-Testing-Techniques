
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.leakyReLU  = nn.LeakyReLU(negative_slope=negative_slope)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = (v1 > 0).to(torch.float32) * -0.7071067811865476 + v1 # Compute a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3 = self.leakyReLU(v2) # Apply the leaky relu function to the result of the multiplication by -0.7071067811865476 based on mask v2
        
        return v3
        
# Initializing the model        
m  = Model()
 
 # Inputs to the model       
x1  = torch.randn(1, 8, 9, 9)
