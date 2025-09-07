
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 4)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model(torch.randn(1, 3, 64, 64))


