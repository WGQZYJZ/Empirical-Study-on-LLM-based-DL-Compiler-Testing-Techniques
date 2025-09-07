
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, ...) # Apply linear transformation to the input tensor.
        return v1.permute(0, 2, 1)


# Initializing the model