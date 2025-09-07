
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 4)
 
    def forward(self, x1):
        v1 = x1.view(-1, 28*28)
        return torch.sigmoid(self.linear(v1))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, 784)
