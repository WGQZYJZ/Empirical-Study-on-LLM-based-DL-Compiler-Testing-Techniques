
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        if other is None:
            other = torch.randn(8, device=x1.device)
        v1 = self.conv(x1) + other
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Keyword argument `other` is set to a tensor with random values from Normal distribution on CPU device.
