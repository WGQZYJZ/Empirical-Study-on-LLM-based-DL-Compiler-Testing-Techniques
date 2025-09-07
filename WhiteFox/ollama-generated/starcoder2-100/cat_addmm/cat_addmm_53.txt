
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim

    def forward(self, x1):
        v1  = torch.addmm(x1[:, :, :], mat1) # Matrix multiplication on a specific axis using mat1 as input and an empty matrix
        v2  = torch.cat([v1], -1) # Concatenate the result along -1
        return v2


# Initializing the model
m = Model()
mat1 = [0,0] + [-34,-57]
__inputs__ = (torch.randn(4, 8), mat1)
