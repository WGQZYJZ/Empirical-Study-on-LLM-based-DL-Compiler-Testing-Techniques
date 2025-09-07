
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1, mat1, mat2): 
        v1 = torch.addmm(x1, mat1, mat2)  # Matrix multiplication
        v2 = torch.cat([v1], dim)  # Concatenation
        return v2

# Initializing the model
m  = Model()


# Inputs to the model (inferred from the user's inputs to the model)
x1 = torch.randn(8, 4, 50)
mat1  = torch.randn(4, 73)
mat2  = torch.randn(73, 97)

 