
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        y = self.linear(x)
        return torch.where(y > 0, y, -y)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
