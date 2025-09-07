
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x):
        v = self.linear(x) + 1 # Add another value to the result of linear transformation
        return v


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
