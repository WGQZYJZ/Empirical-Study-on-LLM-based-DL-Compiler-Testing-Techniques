
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(42895367000, 1)
    
    def forward(self, x1):
       return torch.sigmoid(self.lin(x1))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 42895367000)


