
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(32, 3)
        self.matmul2 = torch.nn.Linear(64, 8)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim)  # Concatenate the result along a specified dimension
        return t2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
