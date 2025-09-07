
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        return l2 / 6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
