
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v = self.linear(x)
        return v * 0.5 + 0.5


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 32, requires_grad=True)
