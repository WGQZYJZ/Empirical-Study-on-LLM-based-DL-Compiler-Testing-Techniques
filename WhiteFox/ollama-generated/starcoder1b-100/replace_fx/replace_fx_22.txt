
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.linear(...)  # Permute x1 with the last two dimensions swapped (this will call the function 'permute' of the input tensor).
        v2 = torch.nn.functional.linear(v1, ...  # Apply linear transformation to the permuted tensor.
        return v2


# Inputs to the model
x1 = torch.randn(1, 3)
