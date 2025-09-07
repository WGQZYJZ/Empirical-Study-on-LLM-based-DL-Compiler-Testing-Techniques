
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v0 = self.linear(x1)
        return torch.clamp_min(v0, -5), \
               torch.clamp_max(v0 + 5, 24)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
__output__, t1 = m(x1) # output 1
t2 = __output__  # output 2 (optional, not required for grad check)

