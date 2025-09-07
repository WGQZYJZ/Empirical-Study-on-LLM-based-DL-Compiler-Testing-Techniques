
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        t1 = torch.addmm(x1, 32.54637991800676, -62) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], self.dim)
        return t2


# Initializing the model
m = Model(dim=1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
