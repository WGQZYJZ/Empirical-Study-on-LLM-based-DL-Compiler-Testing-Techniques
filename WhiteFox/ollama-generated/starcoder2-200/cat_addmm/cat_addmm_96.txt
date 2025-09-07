
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor, mat2: torch.Tensor):
        super().__init__()
        self._mat1 = mat1
        self._mat2 = mat2
 
    def forward(self, input_: torch.Tensor) -> torch.Tensor:
        v1  = torch.addmm(input_, self._mat1, self._mat2) # Perform a matrix multiplication of the input and the matrices and add it to each other 
        return torch.cat([v1], -3)
 
# Initializing the model
mat_shape  = [7,8]
mat1 = torch.randn(size=mat_shape)
mat2 = torch.randn(size=mat_shape)
m = Model(mat1, mat2)

 # Inputs to the model
x1  = torch.randn(5, 64, 64)
 
