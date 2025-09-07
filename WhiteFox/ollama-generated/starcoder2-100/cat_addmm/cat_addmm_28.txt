
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        
    def forward(self, x):
            t1  = torch.addmm(x1, mat1, mat2)
            t2 = torch.cat([t1], dim=dim)
            return t2

# Initializing the model
m = Model()

# Inputs to the model
mat1  = torch.randn(3650, 784) # Initialize a random matrix with shape (3650, 784). The number of rows and columns is different from the previous model. 
x1  = torch.randn(23495, 10, 784) #Initialize another random tensor with shape (23495, 10, 784) which differs from the previous model.
mat2 = mat1 * -3 # Initialize a matrix that is the same as `mat1`, but has all of its values multiplied by -3

 # The model outputs when inputting the initial inputs
__output___ = m(x1)
