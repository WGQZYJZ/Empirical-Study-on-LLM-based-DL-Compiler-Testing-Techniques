
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        v1 = torch.bmm(t1, self.linear_A.weight)
        v2 = torch.matmul(t1, self.linear_B.weight)
        return torch.add(v1, v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 2, 2)
