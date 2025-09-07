
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x): 
        v1  = self.convT(x)
        v2  = torch.sigmoid(v1)
 
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
__input__ = torch.randn(1,8,64,64) # this will work as long as you have an input size of 8x64x64, 3 for the output
