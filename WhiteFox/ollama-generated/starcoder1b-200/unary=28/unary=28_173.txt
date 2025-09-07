
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 3)
 
    def forward(self, x):
        v  = self.linear(x)
        return torch.clamp_min(v, min_value=5) + 2


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(1, 3, 8, 8)
