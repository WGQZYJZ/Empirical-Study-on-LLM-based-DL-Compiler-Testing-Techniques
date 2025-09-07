
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
x1 = torch.randn(4, 2)
