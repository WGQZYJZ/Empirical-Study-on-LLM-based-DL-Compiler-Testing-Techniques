
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28, 10)
 
    def forward(self, x):
        v  = self.linear(x) - 5
        return v


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(32, 28, 28)
