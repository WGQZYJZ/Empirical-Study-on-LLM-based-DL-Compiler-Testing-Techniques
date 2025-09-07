
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1, other):
        return self.linear(x1) - other


# Initializing the model
m = Model()
x1 = torch.randn(1, 32)
other = 0.1
