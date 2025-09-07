
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2, dim):
        super().__init__()
        self.mat1 = mat1
        self.mat2 = mat2
        self.dim = dim
 
    def forward(self, input):
        t1  = torch.addmm(input, self.mat1, self.mat2)  # Add mm operation between a tensor and a matrix
        t2  = torch.cat([t1], self.dim)  # Concatenate the result along a specified dimension
        return t2


# Inputs to the model
x1 = torch.randn(1, 32, 576)
m = Model(torch.randn(8, 32, 576), torch.randn(8, 32, 576), dim=1)
