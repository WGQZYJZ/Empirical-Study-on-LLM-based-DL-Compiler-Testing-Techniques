
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 32)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 - 5


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 10)
