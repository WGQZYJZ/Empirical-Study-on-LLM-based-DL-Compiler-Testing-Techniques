
class Model(torch.nn.Module):
    def __init__(self, min_=0., max_=1.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
        self.min_  = torch.tensor(min_)
        self.max_  = torch.tensor(max_)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        
        # We don't need to generate the clamp_min and clamp_max ops since they are constants
        # These ops should exist in the generated graph:
        #   clamp_min = torch.clamp_min(v1, self.min_) 
        #   clamp_max = torch.clamp_max(clamp_min, self.max_)
        
        return v1
        
# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

