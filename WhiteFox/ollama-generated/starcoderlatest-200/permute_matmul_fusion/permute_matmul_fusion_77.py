
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.bmm(v1, v2)
        return self.linear1(v3) + self.linear2(x1.mean(dim=1).view(-1, 3))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 4, 3)
