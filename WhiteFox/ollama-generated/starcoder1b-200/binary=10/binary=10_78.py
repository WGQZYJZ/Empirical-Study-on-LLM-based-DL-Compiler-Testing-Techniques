
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 3)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 32)
other = torch.randn(32, 3)
