
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1000, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        other = torch.randn(5)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(32, 1000)
