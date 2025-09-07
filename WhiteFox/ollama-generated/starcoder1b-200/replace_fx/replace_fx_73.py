
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(v1, p=0.5, training=False)
        return torch.rand_like(x1, ...).view(1, 3, 3, 3, 2) * v2


# Initializing the model
m = Model()


