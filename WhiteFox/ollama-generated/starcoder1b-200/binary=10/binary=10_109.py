
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
        self.other   = other
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        return v1


# Initializing the model
m = Model()
other = torch.tensor([[1]])
