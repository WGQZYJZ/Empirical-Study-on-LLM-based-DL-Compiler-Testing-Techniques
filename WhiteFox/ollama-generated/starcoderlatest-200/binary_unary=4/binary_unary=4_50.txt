
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + (other if other is not None else torch.randn(64))
        return torch.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32, 16, 16)
other = torch.rand(1, 32, 8, 8)
