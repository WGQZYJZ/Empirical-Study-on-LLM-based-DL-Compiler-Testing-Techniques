
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
        self.mat_mul = torch.nn.Linear(32, 64)
 
    def forward(self, x1, x2):
        v1 = self.mat_mul(x1)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 32)
x2 = torch.randn(64, 32)
