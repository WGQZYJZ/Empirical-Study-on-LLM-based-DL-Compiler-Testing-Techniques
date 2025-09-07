
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=4, out_features=4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m = Model(-10, 10)


