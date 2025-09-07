
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.linear2 = torch.nn.Linear(64, 32)
        self.linear3 = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        v = self.linear1(x)
        v = self.relu(v)
        v = self.linear2(v)
        v = self.relu(v)
        return v


# Initializing the model
m = Model()

