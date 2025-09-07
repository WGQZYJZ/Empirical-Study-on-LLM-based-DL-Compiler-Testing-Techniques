
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=5.):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=16, out_features=32)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        v  = self.linear(x)
        v_c = (v - self.min_value).clamp_min_(0)
        v_m = v.clamp_max_(self.max_value)
        return torch.relu(v_m) * torch.abs(v_c)


# Initializing the model
m = Model()


