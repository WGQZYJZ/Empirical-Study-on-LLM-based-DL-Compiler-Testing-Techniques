
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
    
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.clamp_min(v1, -5) # Clamp the output of the convolution to a minimum value (-5).
        v3  = torch.clamp_max(v2, 7) # Clamp the output of the previous operation to a maximum value (7). 
        return v3 


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 500, 500)


# Outputs from the model
__output__  = m(x1)