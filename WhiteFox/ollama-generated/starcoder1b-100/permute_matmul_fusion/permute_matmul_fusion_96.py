
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(4, 5)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.bmm(v1, self.linear1.weight)
        v3 = torch.bmm(v2, self.linear2.weight)
        return v3


# Initializing the model
m = Model()


