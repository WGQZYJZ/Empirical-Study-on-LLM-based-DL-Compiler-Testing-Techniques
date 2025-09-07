
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Parameter(torch.randn(6, 7))
        self.mat2 = torch.nn.Parameter(torch.randn(8, 9))
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(6, 7)
x2 = torch.randn(8, 9)
x3 = torch.randn(6, 7)
x4 = torch.randn(8, 9)
