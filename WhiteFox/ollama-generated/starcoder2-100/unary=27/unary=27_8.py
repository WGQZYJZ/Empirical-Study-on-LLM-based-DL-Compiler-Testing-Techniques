
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.minval  = torch.randn(0.) 
        self.maxval  = torch.randn(4.)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2  = torch.clamp_min(v1, min=self.minval) #Clamp the output of the convolution to a minimum value
        return torch.clamp_max(v2, max=self.maxval) # Clamp the output of the previous operation to a maximum value


# Initializing the model 
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)