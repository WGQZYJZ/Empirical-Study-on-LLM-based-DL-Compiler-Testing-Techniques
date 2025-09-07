
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v = self.linear(x)
        v += 3
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 5, 5)
