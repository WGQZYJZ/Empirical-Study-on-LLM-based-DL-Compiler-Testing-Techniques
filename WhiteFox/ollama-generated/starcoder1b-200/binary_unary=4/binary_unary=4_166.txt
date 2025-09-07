
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.linear(x) + other
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model()


