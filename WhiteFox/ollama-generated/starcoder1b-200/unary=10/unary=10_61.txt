
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        return self.linear(x) + 3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 10)
