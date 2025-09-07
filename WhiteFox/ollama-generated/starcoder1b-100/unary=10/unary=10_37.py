
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v = self.linear1(x) + 3
        return torch.clamp_min(v, 0) / 6


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3)
