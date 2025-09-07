
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.4)
        t2 = torch.rand_like(x1, requires_grad=True)
        return self.linear(t1 + t2)


# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(1, 2, 2)
