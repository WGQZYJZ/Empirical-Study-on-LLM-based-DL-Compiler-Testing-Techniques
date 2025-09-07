
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, x2, y2, z2):
        v1  = torch.mm(x1, y1)
        v2  = torch.mm(z1, z2)
        v3  = v1 + v2 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(500, 10) # Matrix A (shape [10 x n])
y1  = torch.randn(40, 20)   # Matrix B (shape [n x 20])
z1  = torch.randn(30, 80)   # Matrix C (shape [50 x 70])
x2  = torch.randn(90, 20)   # Matrix D (shape [40 x 20])
y2  = torch.randn(10, 50)   # Matrix E (shape [30 x 80])
z2  = torch.randn(60, 70)   # Matrix F (shape [90 x 70])

 