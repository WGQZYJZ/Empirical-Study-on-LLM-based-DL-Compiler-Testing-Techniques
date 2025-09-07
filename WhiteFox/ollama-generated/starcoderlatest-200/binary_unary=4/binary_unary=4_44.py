
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other  # The keyword argument `other` is added to the output of the linear transformation
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1024)
