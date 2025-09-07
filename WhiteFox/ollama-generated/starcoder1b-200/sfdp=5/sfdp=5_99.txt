
class Model(torch.nn.Module):
    def __init__(self, hidden_size=100):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, hidden_size)
        self.linear2 = torch.nn.Linear(hidden_size, 4)
 
    def forward(self, x):
        v = F.relu(self.linear1(x))
        o = F.relu(self.linear2(v))
        return o

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
