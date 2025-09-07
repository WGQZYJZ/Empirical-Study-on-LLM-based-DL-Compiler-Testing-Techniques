
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.addmm = torch.nn.Linear(8, 16)
        self.concat_dim = dim
 
    def forward(self, x1):
        t1 = torch.addmm(input, mat1, mat2)
        t2 = torch.cat([t1], self.concat_dim)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
