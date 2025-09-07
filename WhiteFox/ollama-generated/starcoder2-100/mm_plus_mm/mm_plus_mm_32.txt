
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1):
        t  = torch.mm(x1, y1) 
        t2  = torch.mm(z1, w1) 
        return t + t2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(300, 350)
y1  = torch.randn(350, 378)
z1  = torch.randn(472, 396)
w1  = torch.randn(396, 487)

__output__  = m(x1, y1, z1, w1)

