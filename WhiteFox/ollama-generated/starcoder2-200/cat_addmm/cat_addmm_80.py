
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1 = torch.randn([432, 576]) # A random matrix of size [432x576]
        self.mat2 = torch.randn([864, 900]) # A random matrix of size [864x900]
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=dim)
        return v2


# Initializing the model
m  = Model() # Initialize a model with the default value for the concatenation dimension
__output__  = m(torch.randn(10, 432))  # This will pass without error and raise an assertion failure because a random tensor of size [10x432] is provided as input.

