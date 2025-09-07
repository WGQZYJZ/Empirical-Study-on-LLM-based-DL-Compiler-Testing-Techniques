
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 1000)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other 
        v3  = self.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(1, 1000) + 0.5 # A random number between (0.49968785 and 1.5020935)
x1 = torch.randn(1, 4096)
__output__  = m(x1)

