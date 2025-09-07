
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 3)
        self.linear_2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2.permute(0, 2, 1))
        v3 = self.linear_1(v2)
        return self.linear_2(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 4, dtype=torch.float64)
x2 = torch.randn(1, 2, 2, dtype=torch.float64)
