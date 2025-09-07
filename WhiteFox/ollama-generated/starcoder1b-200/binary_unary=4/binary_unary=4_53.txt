
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
        self.relu   = torch.nn.ReLU()
        self.other  = other_tensor
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.other
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model(0)

# Inputs to the model
x1 = torch.randn(1, 10)
