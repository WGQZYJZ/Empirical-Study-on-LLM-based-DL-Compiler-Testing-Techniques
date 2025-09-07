
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.clamp(v1, min=min_value, max=max_value)


# Initializing the model
m = Model()

