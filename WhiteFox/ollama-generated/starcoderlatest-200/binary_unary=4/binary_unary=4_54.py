
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model(torch.randn(1, 3))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
