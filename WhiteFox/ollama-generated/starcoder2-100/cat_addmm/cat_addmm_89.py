
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None, dim=0):
        super().__init__()

        if not mat1:
            self.mat1 = torch.randn((48))
        else:
            self.mat1 = mat1
 
        if not mat2:
            self.mat2 = torch.randn(3, 5)
        else: 
            self.mat2 = mat2
         
        self.dim = dim
 
    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2)
        v2 = torch.cat([v1], self.dim)
 
        return v2


# Initializing the model with some random tensors: 
m = Model()

# Inputs to the model
x = torch.randn((48))
