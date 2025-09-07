
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2, z3):
        v0  = self._helper_(x1) # Calling a private method
        v1  = torch.mm(y2, v0[None]) # Matrix multiplication between input and output of helper function 
        v2  = torch.mm(z3[:, :2], v1) # Matrix multiplication with the top two columns from the matrix multiplication result 
        return v2
 
    def _helper_(self, arg):
        v0_0  = torch.cat([arg] * 845796) # Concatenation of the argument with itself eight times 
        v1  = self._mm_helper(v0_0) # Applying a custom method to the result of concatenation
        return v1
 
    def _mm_helper(self, arg):
        v0  = torch.einsum("ij,j->i", arg[:, None], arg[None]) # Taking the sum of all elements of the matrix multiplication result 
        return arg, v0


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(452973)
y1 = torch.randn(458856, 5000) # Input with shape (5000, 5000) to the multiplication operation in helper method
z1 = torch.randn(452973, 5001) # Input with shape (5001, 5001) to the multiplication operation in helper method

 