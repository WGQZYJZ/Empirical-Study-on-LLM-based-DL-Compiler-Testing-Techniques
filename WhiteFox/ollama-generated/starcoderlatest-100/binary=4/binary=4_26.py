
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 8, 10)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1.view(-1, 32*32*8))
        if not isinstance(other, type(None)):
            v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
