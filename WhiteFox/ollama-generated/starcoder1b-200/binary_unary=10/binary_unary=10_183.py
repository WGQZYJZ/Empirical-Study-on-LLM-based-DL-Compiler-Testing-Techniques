
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x2, other):
        v1 = self.linear(x2)
        v2 = v1 + other
        return relu(v2)


# Inputs to the model
x2 = torch.randn(1, 8)
other = torch.randn(1, 1)
