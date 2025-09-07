
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)

    def forward(self, x1):
        t1 = torch.cat([x1, x1, x1], dim=0)
        t2 = t1.view(16)
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m = Model()


