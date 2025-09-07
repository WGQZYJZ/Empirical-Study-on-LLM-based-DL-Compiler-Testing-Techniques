
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 32)
        self.linear2 = torch.nn.Linear(32, 8)
 
    def forward(self, x0):
        v1  = self.linear1(x0)
        v2  = v1 - other
        v3  = torch.relu(v2)
 
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(5, 64, 64, 64)
