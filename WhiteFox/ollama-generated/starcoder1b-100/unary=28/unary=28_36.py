
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=128):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m = Model(min_value=-3, max_value=3)
__output__  = m(x1)


