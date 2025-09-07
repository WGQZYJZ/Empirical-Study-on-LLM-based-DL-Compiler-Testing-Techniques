
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1  = torch.cat([x1, x1, ...], dim=1)
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m = Model()


