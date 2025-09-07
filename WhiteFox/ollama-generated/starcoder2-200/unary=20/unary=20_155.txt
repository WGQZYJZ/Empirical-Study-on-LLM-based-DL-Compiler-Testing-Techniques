
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
 
        v0 = self.convTranspose(x1)
        v1 = torch.sigmoid(v0)
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(32,8,56,56) # random 3d tensor as an input for convTranspose
__output__  = m(x1)
 

