
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        v = self.linear(x.view(-1, 28 * 28))
        v = torch.sigmoid(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(40, 784)
