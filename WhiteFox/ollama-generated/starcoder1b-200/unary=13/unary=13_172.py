
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        y = self.linear(x)
        return self.sigmoid(y)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
