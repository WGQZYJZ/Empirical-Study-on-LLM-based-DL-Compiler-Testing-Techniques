
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.bmm
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = x2.permute(0, 2, 1)
        v1 = self.bmm(t1, t2)
        v2 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 3)
