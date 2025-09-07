
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, x2=None):
        if not hasattr(self, 'inp'):
            self.inp  = torch.rand(x1.size())
        v0 = torch.mm(x1, x2) + inp
        return v0

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(32, 64)
x2  = torch.randn(64, 5) 
 __output__  = m(x1, x2=x2)
