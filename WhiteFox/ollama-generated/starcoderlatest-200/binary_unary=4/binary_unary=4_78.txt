
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 0.7071067811865476 # Add 0.7071067811865476 to the output of the linear transformation
        v3 = torch.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
