
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
x1 = torch.randn(3, 20)
y1 = torch.randn(3, 10)
