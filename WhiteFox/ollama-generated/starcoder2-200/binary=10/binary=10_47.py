
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)

    def forward(self, x1):
        v1 = self.linear(x1)

        other = torch.ones_like(v1).sum() / (3 * v1[0].size(-1))
        
        v2 = v1 + other
        
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 9)
__output__  = m(x1)
