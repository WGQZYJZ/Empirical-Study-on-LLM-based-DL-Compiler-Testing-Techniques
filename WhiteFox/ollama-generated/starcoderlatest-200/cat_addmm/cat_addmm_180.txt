
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.nn.Linear(8, 3)
 
    def forward(self, x1, mat1, mat2, input):
        v1 = torch.addmm(input, mat1, mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim=1) # Concatenate the result along a specified dimension
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(3, 8).to('cuda')
mat2 = torch.randn(8, 3).to('cuda')
