
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.tanh(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 20)
