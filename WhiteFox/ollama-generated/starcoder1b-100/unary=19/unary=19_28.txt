
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 256)
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = torch.sigmoid(t1)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(10, 784)
