
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 28*28))
        v2 = v1 + x2
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 1, 3072)
x2 = torch.randn(5, 6, 3072)
