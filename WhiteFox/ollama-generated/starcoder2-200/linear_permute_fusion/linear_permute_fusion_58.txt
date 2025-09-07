
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear.weight)  # Apply linear transformation to the input tensor.
        v4 = v3.permute(0, 2, 1)                                 # Permute the output tensor of the linear function with more than two dimensions.
        return v4


# Initializing the model