
class Model(torch.nn.Module):
    def __init__(self, sink_cat=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        if self.sink_cat:
            return x1 + x2
        v1  = torch.cat([x1, x2], dim=1)
        v2  = torch.relu(self.linear(v1))
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
