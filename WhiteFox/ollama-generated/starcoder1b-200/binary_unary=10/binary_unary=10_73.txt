
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return self.relu(v1) + other


# Initializing the model
m = Model()


