
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v = self.linear(x) - 0.5
        v = torch.relu(v)
        return v


# Initializing the model
m = Model()

