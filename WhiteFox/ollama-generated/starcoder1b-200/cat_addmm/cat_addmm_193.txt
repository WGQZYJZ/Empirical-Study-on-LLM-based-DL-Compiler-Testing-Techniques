
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 4)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        h1 = self.fc1(x1)
        h2 = self.relu(h1)
        return h2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 8)
