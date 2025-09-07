
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other:
            v2 = v1 + other
        else:
            v2 = v1
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1  = torch.randn(1, 3)
other  = torch.randn(1, 8)
__output__  = Model()(x1, other=other)

