
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3 # Adding a constant of 3 to the output of pointwise convolution operation
        v3  = torch.clamp_min(v2, 0)# Clamping the output of the previous operation to a minimum of zero
        v4  = torch.clamp_max(v3, 6) # Clamp the result of clamping operation to maximum value of 6
        v5  = v4 / 6 
        return v5

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

 