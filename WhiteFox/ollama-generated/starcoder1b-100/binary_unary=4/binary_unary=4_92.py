
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 64 * 3)
 
    def forward(self, x1, other):
        y1 = torch.relu(self.linear(x1))
        return y1 + other


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64 * 64)
other = torch.randn(3, 64 * 3)
