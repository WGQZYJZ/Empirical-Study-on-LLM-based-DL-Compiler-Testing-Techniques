
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x):
        v1  = self.convTranspose(x)
        v2  = v1 + 3 
        v3  = torch.clamp(v2, min=0) 
        v4  = torch.clamp(v3, max=6)  
        v5  = v1 * v4        
        return v5 / 6

# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(2, 3, 90, 78)
__output__  = m(x)

