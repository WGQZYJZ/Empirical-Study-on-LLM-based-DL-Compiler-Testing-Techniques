
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, x1):
        v1 = input_tensor.permute(...)  # Permute the input tensor
        v2 = torch.nn.functional.linear(v1, ...)  # Apply linear transformation to the permuted tensor.
        v3 = torch.nn.functional.dropout(v2)    # Dropout on top of the linear transformed output.
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
