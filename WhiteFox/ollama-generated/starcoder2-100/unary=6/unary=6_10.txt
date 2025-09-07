

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 5 
        v4 = torch.clamp_min(v2,0) # Clamp the output of the addition operation to a minimum of 0
        v3  =torch.clamp_max(v4,6)# Clamp the output of the previous operation to a maximum of 6
        v5 = v1*v3 
        v6 = v5/8 # Divide the result of multiplication by 8. The 8 here is the ReLU6 range (0-6)
        return v6
# Initializing the model
m = Model()

 # Inputs to the model
x1=torch.randn(1,3,64,64)# input to model, 3 - input channels, 64, 64 is shape of input image
