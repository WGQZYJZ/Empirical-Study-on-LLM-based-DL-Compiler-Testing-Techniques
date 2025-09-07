
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        y  = self.linear(x)
        z = other + y
        return z


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(32, 3, 10)
