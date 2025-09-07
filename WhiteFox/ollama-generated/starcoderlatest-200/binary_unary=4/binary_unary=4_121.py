
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other is None:
            v2 = v1 + 1
            v3 = torch.relu(v2)
        else:
            v2 = v1 + other
            v3 = torch.relu(v2)
 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32, 64)
v1 = m(x1) # Apply the linear transformation to x1 (i.e., pass it through the forward function).
