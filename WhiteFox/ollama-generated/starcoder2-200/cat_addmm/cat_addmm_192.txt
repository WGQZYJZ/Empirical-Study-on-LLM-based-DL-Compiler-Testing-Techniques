
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = 0
 
    def forward(self, x1, mat1, mat2):
        v1 = torch.addmm(x1, mat1, mat2) # addmm performs the matrix multiplication of input and matrices and adds it to an output tensor.
        return torch.cat([v1], dim=self.dim)


# Initializing the model with specified dimension
m  = Model()


# Inputs to the model