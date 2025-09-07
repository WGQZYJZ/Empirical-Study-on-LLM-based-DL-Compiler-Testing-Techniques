
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(80 * 2 * 2, 64)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1.view(-1, 80 * 2 * 2))
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.ones_like(x1)
