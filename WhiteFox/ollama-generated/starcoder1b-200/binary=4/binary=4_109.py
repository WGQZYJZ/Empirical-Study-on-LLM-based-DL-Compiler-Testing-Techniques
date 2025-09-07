
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        return v1 + self.other


# Initializing the model
m = Model()


