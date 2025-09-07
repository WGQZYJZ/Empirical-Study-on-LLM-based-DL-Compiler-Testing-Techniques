
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.mat1 = torch.ones(832, 4)
        self.mat2 = torch.zeros((832, 4))
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn((832,)) # Initialize a random 5-dimensional tensor
