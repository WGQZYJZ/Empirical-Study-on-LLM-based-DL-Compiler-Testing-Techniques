
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v = self.linear(x)
        w = self.linear(other)
        return relu(w + other + other * other)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32)
y1 = torch.randn(16)
