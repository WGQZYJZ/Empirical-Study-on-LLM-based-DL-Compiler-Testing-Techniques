
class Model(torch.nn.Module):
    def __init__(self, k1=2):
        super().__init__()
 
    def forward(self, x1, y1):
        v1 = torch.mm(x1, y1)
        v2 = torch.cat([v1] * 5000)
        return v2

# Initializing the model
k1=3 
m = Model(k1=k1)

# Inputs to the model
t3  = torch.randn((8, k1)) # Input tensor of size (8 x 3)
t4  = torch.randn((k1, 7)) # Input tensor of size (3 x 7)
__output__  = m(t3, t4)

