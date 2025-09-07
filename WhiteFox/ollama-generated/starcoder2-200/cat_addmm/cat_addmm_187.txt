
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, mat1, mat2, dim=0):
        v1 = torch.addmm(x1, mat1, mat2) 
        v2  = torch.cat([v1],dim=dim)
        return v2

m = Model()
input = torch.randn(16,3785409)
mat1 = torch.empty(283495, 3785409).normal_(mean=-5., std=1.) # A random tensor of shape (283495, 3785409), normal distribution  mean = -5 standard deviation = 1
mat2 = torch.empty(283495, 3785409).normal_(mean=-5., std=1.) # A random tensor of shape (283495, 3785409), normal distribution mean = -5 standard deviation = 1
dim_axis  = torch.randint(low=0, high=6) # The dimension to concatenate the tensor on
__output__  = m(input, mat1, mat2, dim=dim_axis)

