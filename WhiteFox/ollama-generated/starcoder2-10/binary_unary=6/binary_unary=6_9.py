
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 - other
        v4 = torch.relu(v3)
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model 
x1 = torch.randn(64, 256)
other = torch.rand(1).item() # For example: 0.97821384
