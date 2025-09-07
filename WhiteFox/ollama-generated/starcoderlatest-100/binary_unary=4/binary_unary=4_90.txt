
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if not (other is None):
            v2 = v1 + other
        else:
            v2 = v1 
        return torch.nn.functional.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64)
