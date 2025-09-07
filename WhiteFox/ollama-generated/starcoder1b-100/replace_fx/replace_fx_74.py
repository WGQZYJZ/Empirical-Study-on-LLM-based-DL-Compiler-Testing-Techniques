
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.rand_like(v1, ...)  # Replace a node invoking torch.rand_like by another equivalent replacement.
        return torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)


# Inputs to the model
x1 = ...
