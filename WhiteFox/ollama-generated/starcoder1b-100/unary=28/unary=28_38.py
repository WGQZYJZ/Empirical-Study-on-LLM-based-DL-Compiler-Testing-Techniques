
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1.clamp(min=0., max=1.)
        return v2


# Initializing the model
m = Model(min_value=-1., max_value=1.)


# Inputs to the model
x1 = torch.randn(2, 4)
