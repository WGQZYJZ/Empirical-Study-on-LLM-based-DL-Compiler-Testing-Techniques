
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        y  = torch.addmm(x1, x2, x3) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        z  = torch.cat([y], dim=1)  # Concatenate the result along dimension 0
        return z


# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
