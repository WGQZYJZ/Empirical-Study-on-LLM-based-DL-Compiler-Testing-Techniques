
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2, ..., xN):
        return t1 + t2 + ... + tN


# Initializing the model
m = Model()


