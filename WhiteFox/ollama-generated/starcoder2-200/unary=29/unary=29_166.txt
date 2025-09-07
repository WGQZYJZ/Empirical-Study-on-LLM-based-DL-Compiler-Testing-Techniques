
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(
            in_channels=32, out_channels=8, kernel_size=4, stride=2)
        self.minv = 0.1 # clamping minimum value 
        self.maxv = 65 # clamping maximum value 
 
    def forward(self, x):
 
        v1 = self.conv(x)        
        v2 = torch.clamp_min(v1, min=self.minv)
        v3 = torch.clamp_max(v2, max=self.maxv)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model 
x = torch.randn(160, 8, 957, 427)

# Output of the model with the initial input x
__output__  = m(x).detach().numpy()