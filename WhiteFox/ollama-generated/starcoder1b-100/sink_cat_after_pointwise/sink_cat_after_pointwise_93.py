
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        v1  = x1.permute(0, 2, 1)
        if x2 is not None:
            v2 = torch.cat([x2.view(-1, 2), x2.view(-1, 2)], dim=-1)
            t3 = torch.relu(v2)
        else:
            t3 = torch.relu(v1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(2, 4, 2)
