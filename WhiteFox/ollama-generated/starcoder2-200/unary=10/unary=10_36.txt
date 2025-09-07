
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l = self.l(x1)
        l2  = torch.clamp_min(l + 3, 0) 
        l3  = torch.clamp_max(l2 , 6) 
        l4  = l3 / 6
        return l4

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8*8*10)
__output__  = m(x1)

