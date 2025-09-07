
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.nn.Linear()(x1)
        v2  = torch.nn.add(v0, other)
        return v2


# Initializing the model
m = Model()
other  = torch.randn(4,5) # Any valid tensor
