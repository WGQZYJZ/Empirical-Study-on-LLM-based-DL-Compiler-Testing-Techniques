
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1, other=0):
        v1 = self.linear(x1)
        v2 = v1 + other
        return torch.relu(v2)


# Initializing the model
m = Model(torch.randn(1))


