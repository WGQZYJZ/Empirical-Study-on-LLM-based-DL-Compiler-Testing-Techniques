
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 50)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = x1.view(-1, 784)
        v2 = self.linear(v1)
        return torch.sigmoid(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 784)
