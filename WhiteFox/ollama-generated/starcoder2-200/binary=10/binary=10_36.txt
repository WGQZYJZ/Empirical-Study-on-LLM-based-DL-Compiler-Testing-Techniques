
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + some_other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 32)


# Output of the model
