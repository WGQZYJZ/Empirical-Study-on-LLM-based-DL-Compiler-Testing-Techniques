
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1, other=None):
        v1 = self.linear1(x1)
        if other is not None:
            v2 = self.linear2(other)
            return v1 + v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 32)
