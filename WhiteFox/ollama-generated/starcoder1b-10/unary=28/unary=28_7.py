
class Model(torch.nn.Module):
    def __init__(self, min_value=-1., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)
# Initializing the model
m = Model()


