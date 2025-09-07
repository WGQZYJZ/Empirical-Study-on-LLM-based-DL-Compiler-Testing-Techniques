
class Model(torch.nn.Module):
    def __init__(self, mat1=None):
        super().__init__()
        self._mat1 = torch.randn(50, 784) if not mat1 else mat1
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self._mat1, None) 
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(50, 784)
