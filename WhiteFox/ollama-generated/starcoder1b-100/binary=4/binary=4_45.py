
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 1)
        self.linear2 = torch.nn.Linear(1, 1)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        return self.linear2(torch.tanh(v1))


# Initializing the model
m = Model()
