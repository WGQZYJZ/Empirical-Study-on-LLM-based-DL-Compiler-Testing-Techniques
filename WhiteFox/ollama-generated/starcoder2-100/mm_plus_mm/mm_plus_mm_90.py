
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1, z1, w1, x2, y2, z2, w2):
        v1  = torch.mm(x1, y1) 
        v2  = torch.mm(z1, w1)
        v3  = v1 + v2

        v4  = torch.mm(x2, y2)
        v5  = torch.mm(z2, w2)
        v6  = v4 + v5
        
        return v3, v6

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(800, 300)
y1  = torch.randn(300, 297)
z1  = torch.randn(400, 500)
w1  = torch.randn(297, 500)
x2  = torch.randn(800, 297)
y2  = torch.randn(300, 496)
z2  = torch.randn(400, 500)
w2  = torch.randn(297, 500)

__output__, __output1__ = m(x1, y1, z1, w1, x2, y2, z2, w2)

