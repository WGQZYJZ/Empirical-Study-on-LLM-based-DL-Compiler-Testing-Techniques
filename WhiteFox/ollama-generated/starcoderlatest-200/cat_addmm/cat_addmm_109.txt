
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.tensor([[3], [-2], [5]])
        self.mat2 = torch.tensor([[-4], [7], [-9]])
 
    def forward(self, x1):
        t1 = torch.addmm(x1, self.mat1, self.mat2)
        t2 = torch.cat([t1], dim=0)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
