
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 6)

    def forward(self, x1):
        l1 = self.linear1(x1)
        v2 = torch.clamp(l1 + 3, 0, 6)
        l3 = v2 / 6
        return l3


# Initializing the model
m = Model()


