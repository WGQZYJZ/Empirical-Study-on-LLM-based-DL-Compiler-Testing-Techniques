
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return self.relu(v1)


# Initializing the model
m = Model()

