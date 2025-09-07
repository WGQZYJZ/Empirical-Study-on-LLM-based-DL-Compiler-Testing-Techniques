
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, self.min_value), torch.clamp_max(v1, self.max_value)


# Initializing the model
m = Model()
