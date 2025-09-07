
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(784, 20)
 
    def forward(self, x1):
        v1  = self.lin1(x1)
        v3  = torch.add(v2, 5.)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(64, 784)
