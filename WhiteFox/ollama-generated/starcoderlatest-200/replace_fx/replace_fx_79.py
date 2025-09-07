
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, ...)
        t2 = torch.rand_like(t1, ...)
        return self.linear(t2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
