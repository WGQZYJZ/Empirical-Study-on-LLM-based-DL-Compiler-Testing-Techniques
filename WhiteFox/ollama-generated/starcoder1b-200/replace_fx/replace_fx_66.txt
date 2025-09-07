
class Model(torch.nn.Module):
    def __init__(self, dropout=False):
        super().__init__()

        self.dropout = dropout

    def forward(self, x1):
        if self.dropout:
            return torch.nn.functional.dropout(x1, p=0.5)
        else:
            return torch.rand_like(x1, dtype=torch.float)


# Initializing the model
m = Model()


