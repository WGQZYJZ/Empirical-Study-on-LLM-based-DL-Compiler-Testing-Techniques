
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Parameter(data=torch.rand(6, 8), requires_grad=False) 
        self.mat2 = torch.nn.Parameter(data=torch.rand(7, 9), requires_grad=False)
 
    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2)
        t2 = torch.cat([v1], dim=0) 
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(2, 6, 4, 3, requires_grad=True)
