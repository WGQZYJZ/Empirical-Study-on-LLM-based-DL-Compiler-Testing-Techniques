
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 2, 1)   # Permute the output of the linear function into a new tensor with the order [0 2 1].
        return v2

# Initializing the model