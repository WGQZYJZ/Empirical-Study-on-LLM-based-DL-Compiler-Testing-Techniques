
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 1)
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = t1 + 10
        return torch.relu(t2)


# Initializing the model
m = Model()


