
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.35):
        super().__init__()

        self.conv = torch.nn.ConvTranspose2d(16, 8, 1, stride=2)
        self.negative_slope  = negative_slope
    
    def forward(self, x1):
      v1 = self.conv(x1)
      v2 = (v1 > 0).float() * v1 
      v3 = torch.nn.functional.leaky_relu(input=v1, negative_slope=self.negative_slope )
      v4 = torch.where(condition=v2 == True ,x1=v3) 
      return v4


# Initializing the model 
m = Model()

 # Inputs to the model  
x1 = torch.randn(8, 16, 32, 32)
