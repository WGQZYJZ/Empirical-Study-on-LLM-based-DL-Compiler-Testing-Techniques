
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=1) # clamp minimum value to 0 in this case
        v3 = torch.clamp_max(v2, max=756)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(10, 32)
