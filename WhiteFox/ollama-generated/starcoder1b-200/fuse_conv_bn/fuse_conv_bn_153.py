
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x):
        v = conv(x) # X should match with ConvXd
        v = batch_norm(v)
        return self.linear(v)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, ...) # X can be 1, 2, or 3 representing the dimension
