
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16, bias=False)
 
    def forward(self, x):
        v = self.linear(x) + 3
        v /= 6
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 4)
