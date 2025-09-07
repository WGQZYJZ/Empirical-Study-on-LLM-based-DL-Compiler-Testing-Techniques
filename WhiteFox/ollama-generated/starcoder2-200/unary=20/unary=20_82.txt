
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8,3,1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
__output__  = m(torch.randn(30,8,64,64))
 
 
