
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32*10, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(10, 3, 64, 64)

 # Other tensor inputs to linear transformation (v6 is a constant)
other = torch.zeros(1, 8)
