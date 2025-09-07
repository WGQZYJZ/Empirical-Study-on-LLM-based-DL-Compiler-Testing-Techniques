
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model and supplying an additional tensor `other` for the linear transformation in the model.
m = Model(torch.randn(1, 8))
