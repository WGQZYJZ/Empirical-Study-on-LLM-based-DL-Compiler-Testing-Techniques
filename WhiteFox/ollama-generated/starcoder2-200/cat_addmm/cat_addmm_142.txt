
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.concat = torch.nn.functional.concat
        self.matmul = torch.mm

    def forward(self, mat1, mat2, input):
        t1  = self.matmul(input, mat1) + mat2 # Performs a matrix multiplication of mat1 and mat2 followed by addition with the result to an input tensor
        t2 = self.concat([t1], dim=0) # Concatenate along dimension
        return t2
# Initializing the model
m  = Model(dim=0)


# Inputs to the model
mat1 = torch.randn(3,4)
mat2 = torch.randn(4,5)
input = torch.randn(786, 3, 1, 9)
__output__  = m(mat1, mat2, input)

