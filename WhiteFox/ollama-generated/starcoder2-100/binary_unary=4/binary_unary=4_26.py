
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other if other else v1
        v3 = F.relu(v2)
        return v3


# Initializing the model with `other` parameter set to None.
m = Model()
__output__  = m(torch.randn(1, 32))

