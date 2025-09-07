
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Parameter(
            data=torch.randn(64, 32, 3, 3), requires_grad=True)
        self.mat2 = torch.nn.Parameter(
            data=torch.randn(8, 64, 3, 3), requires_grad=True)
 
    def forward(self, x):
        t1 = torch.addmm(x, self.mat1, self.mat2)
        t2 = torch.cat([t1], dim=-1)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
