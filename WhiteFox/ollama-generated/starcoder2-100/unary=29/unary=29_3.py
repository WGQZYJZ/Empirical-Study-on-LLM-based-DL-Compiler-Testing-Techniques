
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min(**kwargs)) 
        v3 = torch.clamp_max(v2, max(**kwargs))
        return v3


# Initializing the model 
m = Model() 

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64) 

 # The initial input tensor and output of the model. Since the model's parameter is not changed between each execution,
 # we can also specify its inputs as the initial value of the input argument.
