
class Model(torch.nn.Module):
    def __init__(self, splitdim=0):
        super().__init__()
        self.splitdim  = splitdim
 
    def forward(self, x1):
        v3 = torch.cat([v2 for v2 in torch.split(x1, [64] * (98), dim=(self.splitdim))], dim=0)

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(512,)
__output__  = m(x1)

