

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
    
    def forward(self, x1):
        v0 = torch.clamp_min(x1, -5.0)
        v1 = torch.clamp_max(v0,  5.0) 
        return v1

m = Model()

x  = torch.rand(2,3,64,64)*9-5
__output__  = m(x)

# Initializing the model

