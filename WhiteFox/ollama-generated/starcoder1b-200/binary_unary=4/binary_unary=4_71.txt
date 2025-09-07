
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, requires_grad=True)
