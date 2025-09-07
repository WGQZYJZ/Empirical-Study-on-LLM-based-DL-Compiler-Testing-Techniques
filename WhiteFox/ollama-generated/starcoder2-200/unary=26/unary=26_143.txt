
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3921568674993515):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2 = (v1 > 0).float()  
        v4 = -self.negative_slope
        v5 = torch.where(v2 == 1., v1, v4 * v1) 
        return v5
 
# Initializing the model  
m  = Model(.3921568674993515)


# Inputs to the model  
x  = torch.randn(1, 3, 64, 64)  

