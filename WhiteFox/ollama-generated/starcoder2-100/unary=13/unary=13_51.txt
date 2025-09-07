
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048*7*7, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v3 = sigmoid(v1)
        return t3 * v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048*7*7, 4096) 

# Inputs to the model (for gating mechanism)
x2 = torch.sigmoid(torch.normal(mean=torch.zeros((357,)), std=0.1))

__output__  = m(x1)

