
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2, min=0) # clamp minimum at 0
        v4  = torch.clamp_max(v3, max=6) # clamp maximum at 6
        v5  = v4 / 6   # divide by 6
        return v5 


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 8, 32, 32)
__output__  = m(x)


