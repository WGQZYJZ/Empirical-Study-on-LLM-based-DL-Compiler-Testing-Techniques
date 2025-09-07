
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5)
        t2 = torch.rand_like(x1)
        return t2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 2, 2)
