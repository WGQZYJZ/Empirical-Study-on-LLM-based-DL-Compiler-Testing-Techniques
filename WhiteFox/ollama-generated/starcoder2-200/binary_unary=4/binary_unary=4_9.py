
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64, 32)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2  = v1 + other if other is not None else 0.5 * other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
other  = torch.randn(64, 32)
x1  = torch.randn(64, 64, 64, 64)
__output__  = m(x1, other=other)


