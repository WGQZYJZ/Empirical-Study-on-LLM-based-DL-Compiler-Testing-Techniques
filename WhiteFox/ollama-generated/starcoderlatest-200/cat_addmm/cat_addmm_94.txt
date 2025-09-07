
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 40, 3, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        t1 = torch.addmm(x1, m1, m2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=dim) # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model(dim=2)

# Inputs to the model
x1 = torch.randn(1, 10, 36, 36)
x2 = torch.randn(1, 40, 36, 36)
x3 = torch.randn(1, 10, 36, 36)
x4 = torch.randn(1, 10, 36, 36)
