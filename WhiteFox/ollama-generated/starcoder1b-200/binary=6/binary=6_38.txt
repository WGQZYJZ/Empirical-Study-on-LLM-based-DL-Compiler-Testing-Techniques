
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x):
        v1 = self.linear(x) - 10
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 32, 64)
