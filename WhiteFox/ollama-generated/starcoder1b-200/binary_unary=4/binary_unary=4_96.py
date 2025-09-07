
class LinearModel(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(x1) + other
        v2 = relu(v1)
        return v2


# Inputs to the model
input_tensor = torch.randn(4, 3)
other        = torch.randn(4, 8)
__output__   = LinearModel(other)(input_tensor)


