
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        v4 = self.linear1(v3)
        v5 = self.linear2(v4)
        return v5


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
