
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3072, 1548)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = self.relu(v1)
        v3  = v2 * sigmoid(v1)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3072)
 
__output__  = m(x1)
