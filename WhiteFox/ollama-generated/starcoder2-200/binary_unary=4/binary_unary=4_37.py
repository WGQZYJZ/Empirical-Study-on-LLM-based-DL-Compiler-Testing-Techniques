
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v2  = torch.nn.functional.linear(x1) + other if other is not None else 0
        return torch.nn.functional.relu(v2)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 4)

