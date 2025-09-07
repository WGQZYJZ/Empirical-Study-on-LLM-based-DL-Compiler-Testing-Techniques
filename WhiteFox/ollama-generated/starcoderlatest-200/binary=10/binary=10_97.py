
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1.view(-1))
        if other is not None:
            v2 = v1 + other
        return v2


# Inputs to the model
x1 = torch.randn(3, 64, 64)
other_tensor = torch.zeros(1).uniform_() * 2
