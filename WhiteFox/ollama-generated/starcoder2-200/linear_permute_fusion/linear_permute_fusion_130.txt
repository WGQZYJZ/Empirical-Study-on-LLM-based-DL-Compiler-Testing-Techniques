
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor without swapping its dimensions.
        v2 = v1.permute(-2, -1)               # Permute the output of the linear transformation without changing the shape of this tensor.
        return v2

# Initializing the model