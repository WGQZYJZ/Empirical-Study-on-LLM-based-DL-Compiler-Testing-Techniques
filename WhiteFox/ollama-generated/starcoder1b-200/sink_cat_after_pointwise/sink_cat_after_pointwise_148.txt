
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, ..., ...):
        t1 = x1.permute(...)  # Permute the input tensor
        t2 = torch.cat([t1, t2, ...], dim=...)  # Concatenate tensors along a dimension
        return self.linear(t3)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
