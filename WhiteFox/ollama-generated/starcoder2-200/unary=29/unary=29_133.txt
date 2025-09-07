
class Model(torch.nn.Module):
    def __init__(self, minval=0, maxval=-1):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.convt(x)
        v2  = torch.clamp_min(v1, minval=0) 
        v3  = torch.clamp_max(v2, maxval=-1)
        return v3

 # Initializing the model
m  = Model()

 # Inputs to the model
 
__output__  = m(x)
 
