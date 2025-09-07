
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8,3,1,stride=1,padding=0)
 
    def forward(self, x):
        v1  = self.convT(x) 
        v2  = torch.sigmoid(v1)
        return v2 * v1 


# Initializing the model
m = Model()

 # Inputs to the model
    x  = torch.randn(1,8,64,32) 
    __output__  = m(x)
