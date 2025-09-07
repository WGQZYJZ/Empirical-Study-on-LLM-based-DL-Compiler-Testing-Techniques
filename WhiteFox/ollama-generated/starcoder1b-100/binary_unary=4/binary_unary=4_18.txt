
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        return relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 10)
