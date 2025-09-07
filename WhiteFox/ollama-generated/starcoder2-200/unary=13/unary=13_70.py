
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v0 = self.linear(x1) 
        v1 = self.relu(v0)
        v2 = v1 * v1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 32)
  __output__  = m(x1)
