
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.other   = other
 
    def forward(self, x):
        v = self.linear(x) + self.other
        return v


# Initializing the model
m = Model(torch.randn(4, 16))


