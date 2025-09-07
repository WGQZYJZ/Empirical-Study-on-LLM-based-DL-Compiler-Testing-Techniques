
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(500, 3)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
        else:
            v2 = v1
        return v2


# Initializing the model
m = Model()
