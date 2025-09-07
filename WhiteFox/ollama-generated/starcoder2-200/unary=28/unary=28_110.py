
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=-1e-5):
        super().__init__()
        self.linear  = torch.nn.Linear(3*2*2*8, 4)
        self.min_value  = min_value
        self.max_value  = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
__output__  = m(x1)


# Initializing the model
m  = Model()
m  = Model(min_value=-50., max_value=49.)


# Inputs to the model
x1  = torch.randn(1, 3*2*2*8)


