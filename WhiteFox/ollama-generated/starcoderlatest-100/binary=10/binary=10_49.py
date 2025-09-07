
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 784))
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 1, 64, 64)
