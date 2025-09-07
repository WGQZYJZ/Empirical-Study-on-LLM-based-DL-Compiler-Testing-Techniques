
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 1  # Add 1 to the output of the linear transformation
        return torch.relu(v1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
