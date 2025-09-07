
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.relu(v2) # Add relu activation after addition operation
        v4  = torch.clamp(v3, min=0)
        v5  = torch.clamp(v4, max=6) 
        v6  = v1 * v5
        v7  = v6 / 6 
        return v7

 # Initializing the model
m2  = Model()
 
 # Inputs to the model 
 x1  = torch.randn(1,3, 64, 64)
 
 __output__  = m2(x1)

