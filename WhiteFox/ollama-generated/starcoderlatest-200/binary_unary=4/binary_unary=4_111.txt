
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            return v1
 
        t2 = v1 + other
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 4, 64, 64)
