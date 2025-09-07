
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1), x2.permute(0, 2, 1))
        v2 = torch.matmul(v1, self.linear1.weight) + self.linear1.bias
        v3 = torch.nn.functional.linear(v2, self.linear2.weight) + self.linear2.bias
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 3, 3)
