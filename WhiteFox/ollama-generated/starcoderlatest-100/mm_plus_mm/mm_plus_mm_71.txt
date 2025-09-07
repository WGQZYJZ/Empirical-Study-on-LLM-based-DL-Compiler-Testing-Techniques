
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(3, 8)
        self.matmul2 = torch.nn.Linear(4, 6)
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(3, 5)
x3 = torch.randn(8, 5)
