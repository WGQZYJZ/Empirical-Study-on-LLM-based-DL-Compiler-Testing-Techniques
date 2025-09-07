
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 3) # Apply linear transformation on the input tensor.
        v2 = v1.permute(0, 2, 1)               # Permute the output of this linear function.
        return v2


# Initializing the model