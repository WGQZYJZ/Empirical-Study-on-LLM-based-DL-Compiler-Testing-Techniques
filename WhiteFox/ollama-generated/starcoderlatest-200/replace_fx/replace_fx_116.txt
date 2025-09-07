
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5)
        t2 = torch.rand_like(x1)
        self.linear.weight = t1 * t2
        v1 = self.linear(t1)
        return v1


# Generating inputs to the model
x1 = torch.randn(1, 2, 2)
m = Model()
