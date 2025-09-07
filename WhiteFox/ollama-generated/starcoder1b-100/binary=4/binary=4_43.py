
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other_tensor = other_tensor

    def forward(self, x1):
        v1 = self.linear(x1)
        return (v2 + self.other_tensor)

# Inputs to the model
