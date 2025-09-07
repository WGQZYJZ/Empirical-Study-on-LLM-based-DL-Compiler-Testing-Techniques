
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v = self.linear(x)
        w = v > 0
        return v * negative_slope

# Inputs to the model
x = torch.randn(2, 3)
