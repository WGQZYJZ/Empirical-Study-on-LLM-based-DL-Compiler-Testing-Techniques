
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 512)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=0)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 784)
mat1 = torch.randn(784, 512)
mat2 = torch.randn(3900, 512)


