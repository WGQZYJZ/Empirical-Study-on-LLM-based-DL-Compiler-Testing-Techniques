
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v6


# Initializing the model
m = Model()
other_tensor = torch.randn(1, 8, 512, 512)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
