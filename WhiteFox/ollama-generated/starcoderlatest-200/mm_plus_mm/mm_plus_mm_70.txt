
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(32, 64)
        self.matmul2 = torch.nn.Linear(64, 128)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.matmul1(x1)
        v2 = self.matmul2(v1)
        v3 = torch.mm(v2, x2)
        v4 = torch.mm(v2, x3)
        v5 = v3 + v4
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32)
x2 = torch.randn(1, 64)
x3 = torch.randn(1, 32)
x4 = torch.randn(1, 64)
