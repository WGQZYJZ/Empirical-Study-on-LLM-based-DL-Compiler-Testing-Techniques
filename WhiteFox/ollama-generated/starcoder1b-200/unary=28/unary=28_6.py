
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=2.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.clamp_min(v, min_value)
        v = torch.clamp_max(v, max_value)
        return v


# Initializing the model
m = Model()


