
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).view(-1, 2)  # -1 is the first dimension (axis=-1).
        v2 = torch.relu(v1 + x2)             # Apply a pointwise unary operation to the reshaped tensors, as before.
        return v2


# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2 = torch.randn(3, 4, 2)
