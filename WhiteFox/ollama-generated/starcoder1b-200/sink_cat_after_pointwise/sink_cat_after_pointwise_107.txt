
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = self.linear2(v1)
        return v2


# Initializing the model
m = Model()


