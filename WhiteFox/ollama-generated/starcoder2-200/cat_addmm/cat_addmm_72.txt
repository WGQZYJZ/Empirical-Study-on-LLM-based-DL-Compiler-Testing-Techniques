
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
 
    def forward(self, input):
        v1 = torch.addmm(input, mat1, mat2) # Adding two matrices and performing a matrix multiplication using torch.addmm()
        v2 = torch.cat([v1], dim=dim)  # Concatenate the result along the specified dimension. Note that dim is an argument of forward() method
        return v2

# Initializing the model
m = Model(0)
 
# Inputs to the model
input_tensor = torch.randn(5, 4)
