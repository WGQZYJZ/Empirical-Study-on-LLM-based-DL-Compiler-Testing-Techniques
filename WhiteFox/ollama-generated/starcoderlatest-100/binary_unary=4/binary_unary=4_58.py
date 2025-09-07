
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model(torch.randn(10, 3))

# Inputs to the model
x1 = torch.randn(50, 1024)
