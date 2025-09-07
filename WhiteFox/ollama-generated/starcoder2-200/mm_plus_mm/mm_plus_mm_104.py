
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1, z1):
        v1  = torch.mm(x1, y1) 
        v2  = torch.mm(y1, z1)
        v3  = v1 + v2
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(100, 5, 4, 8 ) # shape (100 x 5 x 4 x 8)
y1 = torch.randn(9, 7, 6 ,3) # shape (9 x 7 x 6 x 3)
z1 = torch.randn(9, 5, 7) # shape (9 x 5 x 7)
