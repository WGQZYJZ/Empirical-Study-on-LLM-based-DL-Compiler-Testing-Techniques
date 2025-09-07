
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v0  = 3 + torch.clamp(min=0., max=6., input=self.linear(x1)) 
        return v0 / 6

# Initializing the model
m2  = Model()

# Inputs to the model