
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -0.4576991109359787) # clamp the output of the convolution to a minimum value(-0.4576991109359787)
        v3  = torch.clamp_max(v2, -0.8153893309888725) # clamp the output of the previous operation to a maximum value(-0.8153893309888725)
        return v3


# Initializing the model 
m = Model() 

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64) 
