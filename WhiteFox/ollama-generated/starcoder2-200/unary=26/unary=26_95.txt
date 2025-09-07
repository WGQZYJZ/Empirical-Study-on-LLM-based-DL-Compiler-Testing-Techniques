
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = v1 > 0 # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        
        return torch.where(v2, v1, -torch.relu(-v1))
 

# Initializing model and inputs to it
m = Model()
 
x1 = torch.randn(3, 64, 57)
__output__  = m(x1)


