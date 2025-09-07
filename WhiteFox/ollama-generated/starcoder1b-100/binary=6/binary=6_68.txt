
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 1)
 
    def forward(self, x1):
        v1 = torch.relu(self.linear(x1))
        v2 = v1 - other  # Subtract 'other' from the output of the linear transformation
        return v2


# Initializing the model
m = Model(10)


# Inputs to the model
x1 = torch.randn(1, 64, 64)
