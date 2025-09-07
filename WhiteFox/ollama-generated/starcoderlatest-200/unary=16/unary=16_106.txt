
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28*28, 64)
 
    def forward(self, x1):
        v1 = self.fc1(x1.view(-1, 784))
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 28, 28)
