
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 16)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2)
