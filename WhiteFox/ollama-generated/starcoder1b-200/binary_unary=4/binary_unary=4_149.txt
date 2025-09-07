
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 7 * 7, 32)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other if other is not None else self.linear(x1)
        v2 = relu(v1)
        return v2


# Inputs to the model
x1 = torch.randn(3, 64 * 7 * 7)
other  = torch.randn(25)
