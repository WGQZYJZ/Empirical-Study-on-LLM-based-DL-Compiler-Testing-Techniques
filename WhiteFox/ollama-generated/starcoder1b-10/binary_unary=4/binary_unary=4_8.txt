
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2 = v1 + other  # The `other` keyword argument should be passed here
        return torch.relu(v2)


# Inputs to the model
x1  = torch.randn(1, 16)
