
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):
        v0  = x1 # Input
        v1  = self.conv(v0) 
        v2  = torch.sigmoid(v1)
        return v1*v2


# Initializing the model
m = Model()
 

# Inputs to the model
x1  = torch.randn(1,3,64,64) # Input to the model
