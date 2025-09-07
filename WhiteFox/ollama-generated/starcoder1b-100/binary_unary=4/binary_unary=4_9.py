
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1024)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return self.relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2048, 1024)
other  = torch.randn(1024)
__output__  = m(x1, other)


