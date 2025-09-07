
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1  = self.fc1(x1)
        v2 = v1 * v1
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32, requires_grad=True)
x2 = torch.randn(10, requires_grad=True)
