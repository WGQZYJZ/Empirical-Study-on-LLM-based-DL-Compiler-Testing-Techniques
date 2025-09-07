
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 10)
 
    def forward(self, x):
        y  = self.linear(x) - 1
        return y


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 3, 16, 16)
