
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        v3  = torch.cat([t1, t2], dim=0)
        v4  = v3.view(-1)
        return torch.relu(v4), t2


# Initializing the model
m = Model()

# Inputs to the model
i1 = torch.randn(1)
i2 = torch.randn(5, 1)
__output__, t2 = m(i1, i2)

