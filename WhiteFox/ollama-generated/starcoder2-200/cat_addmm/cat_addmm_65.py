
class Model(torch.nn.Module):
    def __init__(self, mat1: torch.Tensor, mat2: torch.Tensor):
        super().__init__()
        
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v3  = torch.cat([v1], dim=1)  # Concatenate the result along dimension 1
        return v3

# Initializing the model with parameters `mat1` and `mat2`
m = Model(mat1, mat2)

