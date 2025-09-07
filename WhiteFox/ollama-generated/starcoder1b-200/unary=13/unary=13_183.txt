
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 1)
 
    def forward(self, x):
        return sigmoid(self.linear(x))


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(32, 100, 64, 64)
