
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.mat1  = torch.randn(32, 32)
        self.mat2  = torch.randn(32, 512)
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        return torch.cat([v1], dim)


# Initializing the model
m  = Model()
dim  = int(0) 

# Inputs to the model
x1  = torch.randn(32, 512)
__output__  = m(x1)

