
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
        # Parameters to be optimized with `optimizer`
        self._mat1  = torch.nn.Parameter(torch.rand((256*3, 9))) 
        self._mat2  = torch.nn.Parameter(torch.rand((784, 30)))
 
    def forward(self):
        # Inputs to the model
        mat1  = self._mat1.view(-1, 256)
        mat2  = self._mat2

        # Actual model
        t1  = torch.addmm(input=None, mat1=mat1, mat2=mat2) # Perform a matrix multiplication of mat1 and mat2 
        t2  = torch.cat([t1], dim)  # Concatenate the result along a specified dimension
        return t2

# Initializing the model
m = Model()

