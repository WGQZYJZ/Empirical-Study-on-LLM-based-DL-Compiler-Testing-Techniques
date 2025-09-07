
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 32)
v2 = m(x1, other_tensor=torch.randn(8, 64))

