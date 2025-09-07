
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.clamp  = torch.nn.Clamp(min=0, max=6, value=1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return self.clamp(v1 + 3) / 6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4)
