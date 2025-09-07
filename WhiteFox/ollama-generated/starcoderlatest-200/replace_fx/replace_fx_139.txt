
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.1)
        t2 = torch.rand_like(x1, dtype=torch.float32)
        return self.linear(t1), t2

# Initializing the model
m = Model()
m.eval()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
output, _ = m(x1)

