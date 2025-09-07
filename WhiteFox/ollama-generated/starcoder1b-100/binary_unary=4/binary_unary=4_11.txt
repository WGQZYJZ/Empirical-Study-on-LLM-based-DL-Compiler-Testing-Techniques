
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 257, 10)
 
    def forward(self, x1, other=None):
        return self.linear(x1 + other)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64 * 257)
