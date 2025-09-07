
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Linear(3, 8)
        self.mat2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        v1 = self.mat1(x1)
        v2 = self.mat2(v1)
        return torch.mm(v2, x2)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 1, 1)
