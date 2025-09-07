
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, mat1, mat2):
        t1 = torch.addmm(input, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim=2)       # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.ones_like(x1)
mat2 = x1 * 2 + mat1 # x1*2 is equal to mat1*2 so there's no need to multiply the input by 2 for a matrix multiplication and then adding it again (as long as it is used beforehand).
