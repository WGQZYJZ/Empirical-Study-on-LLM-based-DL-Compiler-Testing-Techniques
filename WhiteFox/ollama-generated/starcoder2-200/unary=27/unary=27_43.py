
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
        v1 = self.conv(x) 
        v2 = torch.clamp_min(v1, -0.5).to(torch.float64) # Clamp the output of the convolution to a minimum value (-0.5) and cast it to double precision number for further operation with 3rd party APIs
        v3 = torch.clamp_max(v2,  0.5).to(torch.float16) # Clamp the output of the previous operation to a maximum value (0.5) and cast it to half-precision floating point number for 3rd party APIs
        return v3


# Initializing the model
m = Model()

# Inputs to the model