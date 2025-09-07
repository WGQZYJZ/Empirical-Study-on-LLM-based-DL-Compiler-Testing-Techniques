
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64, 1)

    def forward(self, x1, other=None):
        v0 = F.dropout(x1[0], p=0.5)
        v1 = self.linear(v0).view(-1, 1)
        if other is not None:
            v2 = other * v1
            return [v1 + v2]
        else:
            return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 64)
other  = torch.zeros(8).view(-1,1)

__output__  = m(x1)
