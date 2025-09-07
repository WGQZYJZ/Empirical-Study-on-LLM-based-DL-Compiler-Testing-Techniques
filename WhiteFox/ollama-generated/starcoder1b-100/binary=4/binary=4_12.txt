
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other  # Add the output of the linear transformation to the output of the previous layer
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
