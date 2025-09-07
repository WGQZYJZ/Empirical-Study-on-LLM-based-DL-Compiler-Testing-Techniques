
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        v = self.linear(x)
        return torch.clamp_min(v, self.min_value)


# Initializing the model
m = Model()


