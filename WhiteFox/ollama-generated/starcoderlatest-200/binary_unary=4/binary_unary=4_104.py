
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is not None:
            self.linear = torch.nn.Linear(80, 128)
        else:
            self.linear = torch.nn.Linear(32, 128)
 
    def forward(self, x1):
        t1 = self.linear(x1)
        if other is not None:
            v2 = t1 + other
        else:
            v2 = t1
        v3 = torch.nn.functional.relu(v2)
        return v3
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
