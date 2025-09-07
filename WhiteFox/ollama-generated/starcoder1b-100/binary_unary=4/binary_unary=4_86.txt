
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 256)
        if other:
            self.other = torch.nn.Linear(1024, 256)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        return v3 + other


# Initializing the model
m = Model()

