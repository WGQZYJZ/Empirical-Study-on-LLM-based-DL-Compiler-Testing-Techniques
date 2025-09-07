
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.linear2 = torch.nn.Linear(5, 3)

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.linear2(v1)
        return v2


# Initializing the model
m = Model()


