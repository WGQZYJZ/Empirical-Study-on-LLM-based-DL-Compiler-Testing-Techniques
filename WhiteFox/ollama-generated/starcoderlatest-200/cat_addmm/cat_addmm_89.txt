
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.input = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.mat1 = torch.tensor([
            [1, -1], [-1, 1]
        ])
        self.mat2 = torch.tensor([[2, -2]])
 
    def forward(self, x1):
        t1 = torch.addmm(x1, self.mat1, self.mat2)
        t2 = torch.cat([t1], dim=dim)
        return t2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
