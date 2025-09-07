
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.addmm(input=x1, mat1=mat1, mat2=mat2)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim)  # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(3, 8).view(-1, 1) # mat1 is a 2-D tensor with shape (3, 1) that contains random values in the range [-1, 1]
mat2 = torch.randn(2, 64).permute(0, 3, 1, 2) # mat2 is a 4-D tensor with shape (2, 64, 64, 3) that contains random values in the range [-1, 1]
