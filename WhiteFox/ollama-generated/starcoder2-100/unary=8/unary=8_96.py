
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3 
        v3  = F.relu6(v2) 
        v4  = torch.clamp(v3, min=0., max=6.) 
        v5  = v1 * v4
        v6  = F.linear(v5, v3, bias=None).permute((0, 3, 1, 2))
        return v6


# Initializing the model: 
m = Model() 

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 
__output__  = m(x1)
