
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.cat([t1, t2], dim=3)
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m = Model()


