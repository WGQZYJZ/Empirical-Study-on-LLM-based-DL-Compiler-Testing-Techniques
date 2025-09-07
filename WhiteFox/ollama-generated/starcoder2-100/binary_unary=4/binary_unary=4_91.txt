
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(10, 8)

    def forward(self, x1, other):
        v1  = self.lin(x1)
        v2  = v1 + other 
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
other  = torch.tensor([0., .1])
__output__  = m(torch.randn(4, 10), other=other) # Generates output.

# Inputs to the model
x2  = torch.randn(4, 50)

