
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(20, 516)
 
    def forward(self, x):
        v0 = self.linear(x)
        v1 = v0 *  clamp(min=0., max=3.) + 3
        v2 = v1 / 6
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(4, 18)
