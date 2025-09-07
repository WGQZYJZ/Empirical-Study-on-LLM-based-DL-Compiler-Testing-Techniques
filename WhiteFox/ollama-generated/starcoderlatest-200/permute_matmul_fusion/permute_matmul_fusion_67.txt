
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 5)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        v4 = torch.nn.functional.linear(v3, self.linear1.weight, self.linear1.bias)
        v5 = torch.nn.functional.linear(v4, self.linear2.weight, self.linear2.bias)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
