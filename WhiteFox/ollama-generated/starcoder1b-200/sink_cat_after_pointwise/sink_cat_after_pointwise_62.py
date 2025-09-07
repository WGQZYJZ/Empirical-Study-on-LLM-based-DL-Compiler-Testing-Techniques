
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        t1 = torch.cat([x1, x2], dim=-1)
        t2 = t1.view(-1, 4)
        t3 = torch.relu(t2)

        # Do not forget to return `t3`!
        return t3


# Initializing the model
m = Model()


__inputs__ = ...
