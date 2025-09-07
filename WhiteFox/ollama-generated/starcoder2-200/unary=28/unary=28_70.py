
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v1  = self.linear(x2)
        v3  = torch.clamp_min(v1, min=5) 
        return torch.clamp_max(v3, max=5)


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(49, 784)
__output__  = m(x2)