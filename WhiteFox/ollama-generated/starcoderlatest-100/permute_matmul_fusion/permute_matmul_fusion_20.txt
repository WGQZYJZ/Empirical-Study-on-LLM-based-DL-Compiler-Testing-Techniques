
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.nn.Linear(2, 3)
        self.bmm2 = torch.nn.BMM(2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = x2.permute(0, 2, 1)
        v3  = torch.bmm(v1, v2)
        return torch.matmul(self.matmul1(v3), self.bmm2(v3))


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(1, 4, 3)
