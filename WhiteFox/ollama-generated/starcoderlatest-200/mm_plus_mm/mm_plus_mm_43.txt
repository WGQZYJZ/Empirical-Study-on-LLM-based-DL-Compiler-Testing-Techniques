
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Linear(2048, 512)
        self.mat2 = torch.nn.Linear(512, 384)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.mat1(x1)
        v2 = self.mat2(v1)
        v3 = self.mat1(x2)
        v4 = self.mat2(v3)
        v5 = self.mat1(x3)
        v6 = self.mat2(v5)
        v7 = torch.mm(v2, v6) + torch.mm(v4, v6) + torch.mm(v1, v4) # Addition of the results from the matrix multiplications in each case
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 5024)
x2 = torch.randn(369, 2048)
x3 = torch.randn(369, 2048)
x4 = torch.randn(8, 384)
