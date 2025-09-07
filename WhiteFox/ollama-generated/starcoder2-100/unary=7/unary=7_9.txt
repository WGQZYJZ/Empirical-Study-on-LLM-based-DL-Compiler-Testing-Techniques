
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 * torch.clamp(min=0, max=6, tensor=(v1 + 3)) / 6
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(45, 20)
