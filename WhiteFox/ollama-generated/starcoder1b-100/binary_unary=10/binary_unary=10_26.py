
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.relu(v + other)


# Initializing the model
m = Model()


