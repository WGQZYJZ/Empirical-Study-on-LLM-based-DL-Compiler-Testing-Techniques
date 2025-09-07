
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x):
        v1 = self.linear(x) + 2
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3, 4)
