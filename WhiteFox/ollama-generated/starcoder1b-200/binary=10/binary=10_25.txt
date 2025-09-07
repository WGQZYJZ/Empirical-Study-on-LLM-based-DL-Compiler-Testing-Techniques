
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.linear_1 = torch.nn.Linear(8, 8)
        self.linear_2 = torch.nn.Linear(8, 4)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self.other
        return v2


# Initializing the model
m = Model()
x = torch.randn(1, 3)
