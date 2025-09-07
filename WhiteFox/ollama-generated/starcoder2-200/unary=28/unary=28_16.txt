
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 250)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=1.7976931348623158e+308) # clamp 0
        v3 = torch.clamp_max(v2, max=1.7976931348623158e+308) 
        return v3

# Initializing the model
m = Model()

