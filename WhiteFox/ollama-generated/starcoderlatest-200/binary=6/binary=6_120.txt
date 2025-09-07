
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
 
    def forward(self, x2):
        v3 = self.linear(x2)
        v4 = v3 - 1
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(1, 16, 1, 1)
