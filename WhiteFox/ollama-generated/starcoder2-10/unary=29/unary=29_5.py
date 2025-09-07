
class Model(torch.nn.Module):
    def __init__(self, minValue = 0.1, maxValue = 254):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(3,8,7)
 
    def forward(self, x1):
        v1 = self.convTranspose(x1)
        v2 = torch.clamp_min(v1, minValue) # clamp the output of transposed convolution to a minimum value
        v3 = torch.clamp_max(v2, maxValue) # clamp the previous output to a maximum value
        return v3


# Initializing the model with specified inputs for the clamped operation
clampMinValue  =  10;  # minimum clamping value of input tensor
clampMaxValue  =  5478 ;  # maximum clamping value of input tensor
 
m  = Model(minValue=clampMinValue, maxValue=clampMaxValue)


# Inputs to the model (for specifying the operation clamped operation to a particular value )
x1 = torch.randn(32 , 65 , 78 , 90)

 # Clamping the operation to minimum and maximum values specified above for each respective output. 
 
