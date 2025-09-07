
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 8)
 
    def forward(self, x1):
        v2 = self.linear(x1)
        v3 = v2 - 5497 # other
        v4 = F.relu(v3)
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(60, 30)
__output__  = m(x1)

