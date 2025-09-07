
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.MM(3, 4)
 
    def forward(self, x1, y1, z1, x2, y2, z2):
        v1  = self.mm(x1,y1)
        v2  = self.mm(z1,y2) # Same as torch.mm()
        v3  = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 8)   # Input tensor for the first matrix multiplication
y1  = torch.randn(7, 5)   # Input tensor for the first matrix multiplication
z1  = torch.randn(9, 3)   # Input tensor for the second matrix multiplication
x2  = torch.randn(8, 6)   # Input tensor for the second matrix multiplication
y2  = torch.randn(5, 4)   # Input tensor for the second matrix multiplication
z2  = torch.randn(3, 7)    # Input tensor for the second matrix multiplication

__output__  = m(x1, y1, z1, x2, y2, z2)

