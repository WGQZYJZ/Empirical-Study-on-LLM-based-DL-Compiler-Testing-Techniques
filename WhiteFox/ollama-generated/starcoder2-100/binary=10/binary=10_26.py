
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(56, 10)
other = torch.randn(3, 10).to('cpu') # A random tensor of shape [3, 10] with the CPU device
