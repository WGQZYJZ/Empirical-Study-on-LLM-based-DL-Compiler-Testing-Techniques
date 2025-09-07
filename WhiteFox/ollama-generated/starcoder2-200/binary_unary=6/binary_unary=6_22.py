
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) - other
        v2 = F.relu(v1) # Replace torch.relu with torch.nn.ReLU to fix the issue
        return v2


# Initializing the model
m = Model()


# Inputs to the model