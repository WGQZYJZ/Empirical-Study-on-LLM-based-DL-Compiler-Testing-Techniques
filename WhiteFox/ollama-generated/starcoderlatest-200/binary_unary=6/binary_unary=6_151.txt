
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 784))
        v2 = v1 - 0.5
        v3 = torch.nn.ReLU()(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
