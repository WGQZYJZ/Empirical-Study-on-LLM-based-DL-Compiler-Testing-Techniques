
class Model(torch.nn.Module):
    def __init__(self, max=None, min=None):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32*8 + 16*16*4+ 576, 9)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, min=None)  
        v3  = torch.clamp_max(v2, max=None)  
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64*8 + 576, 9) # shape = (32 * 32 * 8 + 16 * 16 * 4 + 576,)
