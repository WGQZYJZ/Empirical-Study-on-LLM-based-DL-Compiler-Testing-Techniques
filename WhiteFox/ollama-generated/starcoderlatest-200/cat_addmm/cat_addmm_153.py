
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, mat1, mat2)
        t2 = torch.cat([t1], dim=dim)
        return t2
# Initializing the model
m = Model()
# Inputs to the model
mat1 = torch.randn(8, 3, 64, 64) # A matrix of shape [8, 3, 64, 64] is randomly initialized
mat2 = torch.randn(1, 3, 64, 64) # A matrix of shape [1, 3, 64, 64] is randomly initialized
dim = 0 # Set dim=0 for concatenating along the first dimension; set dim=-1 for concatenating along the last dimension.
