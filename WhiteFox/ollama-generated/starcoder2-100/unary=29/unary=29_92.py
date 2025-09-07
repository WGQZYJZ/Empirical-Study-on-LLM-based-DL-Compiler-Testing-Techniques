
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=0)
    
    def forward(self, x):
       v7  = x
       v6  = self.conv(v7)
       v5  = self.convt(v6)
       v1 = torch.clamp_min(v5, min=-3.) 
       v4 = torch.clamp_max(v1, max=20.)
       return v4


# Initializing the model
m  = Model()

# Inputs to the model
x = torch.randn(1, 3, 8, 7)
__output__  = m(x)

