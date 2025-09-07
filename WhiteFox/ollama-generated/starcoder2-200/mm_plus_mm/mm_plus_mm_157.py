
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1):
        v1  = torch.mm(x1, y1)
        v2  = torch.mm(z1, y1)
        v3  = v1 + v2
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(4096, 512)  
y1  = torch.randn(512, 800)  
z1  = torch.randn(512, 372)
__output__  = m(x1, y1, z1)

