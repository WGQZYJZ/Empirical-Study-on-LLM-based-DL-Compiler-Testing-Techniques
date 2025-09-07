
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        return torch.cat([v1] * len(torch.arange(30)), dim=1)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(456, 789)
x2  = torch.randn(456, 987)
