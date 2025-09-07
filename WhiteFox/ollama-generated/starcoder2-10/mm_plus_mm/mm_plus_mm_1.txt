
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1, z1):
        v1  = torch.mm(x1, y1) 
        v2  = torch.mm(z1, y1)

        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3072) # 3x3 matrix: 9 elements, 3 rows and columns.
y1  = torch.randn(3*9)
z1  = torch.randn(3*9)
