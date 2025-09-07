

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.mm(x1)
        v2  = torch.cat([v1]) 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4096, 8753)
__output__  = m(x1)

