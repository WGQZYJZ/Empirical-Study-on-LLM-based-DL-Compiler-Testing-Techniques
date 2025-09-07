
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
        self.add = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.add
        return v2


# Initializing the model
m = Model(torch.tensor([[1.]]))
