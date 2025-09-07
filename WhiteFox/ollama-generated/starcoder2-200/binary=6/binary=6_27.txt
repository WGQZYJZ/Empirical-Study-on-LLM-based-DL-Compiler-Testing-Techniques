
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(24, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 0.576396525785923
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 24)
__output__  = m(x1)