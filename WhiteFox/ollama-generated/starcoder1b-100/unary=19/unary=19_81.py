
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 4)
 
    def forward(self, x1):
        v1 = x1.view(-1, 784)
        v2 = self.linear(v1)
        return torch.sigmoid(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 784).view(1, -1, 28, 28)
