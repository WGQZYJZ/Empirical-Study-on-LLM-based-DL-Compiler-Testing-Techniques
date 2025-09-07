
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=10.0):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=3, out_features=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.clamp_min(v, self.min_value)
        v = torch.clamp_max(v, self.max_value)
        return v


# Initializing the model
m = Model(max_value=200.0)

