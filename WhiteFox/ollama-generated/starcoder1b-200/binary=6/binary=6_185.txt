
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
 
    def forward(self, x):
        y  = self.linear(x) - 3
        return y


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 4)
