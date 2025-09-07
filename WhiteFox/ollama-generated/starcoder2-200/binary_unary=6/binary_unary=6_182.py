
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)

    def forward(self, x):
        v1 = self.linear(x)
        return v1 - 7 + torch.relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(10, 32)
__output__  = m(x)
