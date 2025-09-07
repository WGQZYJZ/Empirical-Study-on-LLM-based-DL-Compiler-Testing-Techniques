
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = x1.permute(...)
        t2 = x2.permute(...)
        out = torch.bmm(t1, t2)
        out = torch.matmul(out, self.linear.weight)
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 4, 2)
