
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ..., xn): # Number of inputs to the model can be greater than two (as long as one input is cat'ed with another)
        t1 = torch.cat([x1, x2, ...], dim=...)
        t2 = t1.view(...)
        t3 = torch.relu(t2)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 4, 2) # One of two inputs can be cat'ed with x1 or x2
...
xn = torch.randn(3, 8, 2)
