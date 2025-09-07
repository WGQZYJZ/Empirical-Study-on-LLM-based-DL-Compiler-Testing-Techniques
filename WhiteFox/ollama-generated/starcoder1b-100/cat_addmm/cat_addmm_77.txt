
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v = self.fc1(x)
        return torch.addmm(v, self.weights, self.bias)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 8)
x2 = torch.randn(3, 4)
