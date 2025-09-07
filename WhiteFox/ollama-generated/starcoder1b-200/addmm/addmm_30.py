
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(4, 4)
        self.m2 = torch.nn.Linear(4, 4)
 
    def forward(self, x1, x2=None):
        if x2 is not None:
            v1 = self.m1(x1)
            v2 = self.m2(x2)
            inp = v2 + x1
            return v1, inp
 
        # if not, then use the default value (0). If this does not work,
        # please make sure you specify your input tensors by yourself.
        else:
            v1 = self.m1(x1)
            return v1


# Initializing the model
m = Model()


# Inputs to the model
inp1 = torch.randn(4, 4)
