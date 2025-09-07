
class Model(torch.nn.Module):
    def __init__(self, min_value=-2., max_value=3.):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=1, out_features=1, bias=False)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        return self.linear(x1) + 2 * self.linear(x1) - self.linear(x1) * self.linear(x1)
 
    def __call__(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


# Initializing the model
m  = Model()


