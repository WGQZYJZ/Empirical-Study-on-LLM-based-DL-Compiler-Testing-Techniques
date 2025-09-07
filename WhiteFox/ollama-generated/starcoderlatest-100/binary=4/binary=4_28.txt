
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + v6
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
other = torch.rand((1, 16))
