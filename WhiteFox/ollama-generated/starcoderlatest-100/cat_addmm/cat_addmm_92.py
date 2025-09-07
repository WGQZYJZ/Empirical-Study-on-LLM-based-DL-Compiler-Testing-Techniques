
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.t1 = torch.nn.Parameter(torch.rand(3))  # A three-dimensional tensor of dimension (80, 30) with a random value initialized to a distribution
        self.mat1 = torch.nn.Parameter(torch.randn(4, 6).transpose(-2, -1))  # A two-dimensional parameter matrix of shape (6, 30) with random values
        self.t2 = torch.nn.Parameter(torch.rand(5))
        self.mat2 = torch.nn.Parameter(torch.randn(dim, dim).transpose(-2, -1))
 
    def forward(self):
        t1 = torch.addmm(input, mat1, mat2)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim)  # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64).requires_grad_()
