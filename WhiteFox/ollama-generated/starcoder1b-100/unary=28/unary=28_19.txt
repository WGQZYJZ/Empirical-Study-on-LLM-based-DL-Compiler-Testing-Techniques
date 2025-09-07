
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        t1 = self.linear(x1)
        return torch.clamp_min(t1, self.min_value), torch.clamp_max(t1, self.max_value)


# Initializing the model
m  = Model(-30, 50)


