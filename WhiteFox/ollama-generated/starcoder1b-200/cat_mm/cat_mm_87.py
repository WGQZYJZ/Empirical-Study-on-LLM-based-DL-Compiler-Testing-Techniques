
class Model(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        # Matrix multiplication of two input tensors
        v = torch.mm(x1, x2)  # Concatenation along the last dimension
        # ...
        return v


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
