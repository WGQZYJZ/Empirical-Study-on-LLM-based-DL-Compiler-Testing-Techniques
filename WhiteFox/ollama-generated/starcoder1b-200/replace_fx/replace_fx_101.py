
class Model(torch.nn.Module):
    def __init__(self, dropout):
        super().__init__()
        self.dropout = torch.nn.functional.dropout if dropout else None
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        if self.dropout is not None:
            v2 = self.dropout(v1)
        else:
            v2 = torch.rand_like(v1, ...)
        return v2


# Initializing the model with dropout
m = Model()


