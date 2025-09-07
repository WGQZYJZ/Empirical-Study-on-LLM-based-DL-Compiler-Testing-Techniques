
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 8)

    def forward(self, x1, other=torch.ones(1)):
        v1 = self.linear1(x1) + other
        v2 = v1 * v1
        return v2


# Initializing the model
m = Model()
