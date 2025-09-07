
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.sigmoid(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4)
