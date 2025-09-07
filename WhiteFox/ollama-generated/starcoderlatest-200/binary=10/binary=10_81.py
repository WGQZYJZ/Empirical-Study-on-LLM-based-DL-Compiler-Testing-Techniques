
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x2, other=None):
        v1 = self.linear(x2)
        if other is not None:
            v2 = v1 + other
        return v2


# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
other_tensor = torch.zeros(1, 16, dtype=torch.float32, requires_grad=True)
