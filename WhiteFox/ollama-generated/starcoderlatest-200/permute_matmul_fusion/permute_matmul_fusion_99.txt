
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        if (v1 == v2).all():
            return torch.bmm(v1, self.linear.weight)
        else:
            return torch.matmul(v1, v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 2, 3)
