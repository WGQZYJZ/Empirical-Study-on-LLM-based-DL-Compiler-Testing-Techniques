
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
x1 = torch.randn(1, 4, 2)
