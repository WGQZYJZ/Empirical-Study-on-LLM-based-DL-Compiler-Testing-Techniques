
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = nn.Dropout(...)
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.dropout(v1)
        return torch.rand_like(v2, ...)


# Initializing the model
m = Model()


