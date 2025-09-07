
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.concat = torch.nn.Concat(dim)
 
    def forward(self, x1, mat1, mat2):
        v1  = torch.addmm(x1, mat1, mat2)
        v3  = self.concat([v1])
        return v3

# Initializing the model and setting the value for dim
m = Model(dim=1)

 # Inputs to the model
x1 = torch.randn(10, 5)
mat1 = torch.randn(20, 10)
mat2 = torch.randn(10, 40)

 