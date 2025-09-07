
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        v3 = relu(v2)
        return v3


# Initializing the model
other = torch.tensor([0.5, 0.6], dtype=torch.float).view(-1, 1, 1)
m = Model(other)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
