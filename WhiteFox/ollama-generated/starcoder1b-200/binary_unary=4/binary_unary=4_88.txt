
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)
        self.relu   = torch.nn.ReLU()
        self.other  = other
 
    def forward(self, x):
        v1  = self.linear(x) + self.other
        v2  = self.relu(v1)
        return v2


# Initializing the model
m = Model()

