
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
        self.mat1 = torch.nn.Parameter(
            data=torch.randn((320*64, 8 * 8)), 
            requires_grad=True) if mat1 is None else mat1 
        self.mat2 = torch.nn.Parameter(
            data=torch.randn(320*576), 
            requires_grad=True) if mat2 is None else mat2
 
    def forward(self, x):
        v1  = torch.addmm(x, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2  = torch.cat([v1], dim=0) # Concatenate the result along a specified dimension
        return v2


# Initializing the model