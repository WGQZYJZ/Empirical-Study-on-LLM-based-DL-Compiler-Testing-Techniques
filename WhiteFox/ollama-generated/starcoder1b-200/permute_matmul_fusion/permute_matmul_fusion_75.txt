
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)
        self.linear_B = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, self.linear_A.weight, self.linear_B.weight)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 5)
x2 = torch.randn(2, 3, 4)
