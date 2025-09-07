
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        return v2


# Inputs to the model
x1 = torch.randn(32, 32, dtype=torch.double)
