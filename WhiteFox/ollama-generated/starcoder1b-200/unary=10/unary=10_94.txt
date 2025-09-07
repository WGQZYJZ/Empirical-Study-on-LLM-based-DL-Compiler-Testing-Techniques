
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v = self.linear(x) + 3
        return torch.clamp_min(v, 0), torch.clamp_max(v, 6) / 6


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 20, 10)
