
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x):
       v1 = self.conv(x) 
       v2 = v1 + 3 # Add 3 to the output of the convolution
       v3 = torch.clamp_min(v2,0) # Clamp the result from previous operation to a minimum value of `0` 
       v4 = torch.clamp_max(v3,6) # Clamp the output from the previous operation to a maximum value of 6
       v5 = v4 / 6 # Divide the output by 6
       
       return v5

# Initializing model
m = Model()

 # Inputs to the model
x1 = torch.randn(1,3,256,256)
__output__  = m(x1)