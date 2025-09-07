
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)

    def forward(self, x1):
        v0 = self.linear(x1)
        return F.leaky_relu(v0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(16, 4) # A random tensor of shape (batch size, dimensionality of input layer). 

