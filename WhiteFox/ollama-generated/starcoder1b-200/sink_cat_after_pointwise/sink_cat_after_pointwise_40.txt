
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, ...):
        t1 = x1.permute(0, 2, 1)
        t3 = torch.relu(torch.cat([t1, t2, ...], dim=1))
        return t3


# Initializing the model
m = Model()


