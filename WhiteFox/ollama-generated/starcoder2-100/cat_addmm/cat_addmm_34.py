
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2) # Apply matrix multiplication of mat1 and mat2 to the input tensor
        return torch.cat([v1], dim=1)
 
# Initialize model
m = Model()

# Inputs to the model 
input_tensor = torch.randn(500000, 384, 64, 64) # The input of the matrix multiplication
mat1 = torch.randn(27000, 90, 512) # Tensor used in the matrix multiplication as a first argument to addmm
mat2 = torch.randn(27000, 384, 512) # Tensor used in the matrix multiplication as a second argument to addmm
 
