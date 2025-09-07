
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.linear = torch.nn.Linear(32016, 3)
        if other_tensor:
            self.other_tensor = torch.nn.Parameter(other_tensor)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other_tensor
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model and its keyword argument
m  = Model()
m = Model(torch.randn(3, device='cpu'))

