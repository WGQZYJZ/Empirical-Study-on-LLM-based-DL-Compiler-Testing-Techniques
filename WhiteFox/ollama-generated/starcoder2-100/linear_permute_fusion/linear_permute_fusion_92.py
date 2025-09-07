
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear)  # Apply the linear transformation to input tensor.
        v2 = v3.permute(0, 2, 1)  # Permute the permuted output tensor from the linear function.
        return v2


# Initializing the model