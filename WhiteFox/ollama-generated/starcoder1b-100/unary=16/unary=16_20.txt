
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.relu(v)


# Initializing the model
m = Model()


