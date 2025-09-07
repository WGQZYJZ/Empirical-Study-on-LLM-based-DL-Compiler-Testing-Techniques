
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        return v2


m  = Model() # initialize the model
 

# Inputs to the model:
x1 = torch.randn(3,8,64,64) 
 
__output__  = m(x1)