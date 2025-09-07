
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(-2, -1)               # Permute the output of linear function.
        return v2


# Initializing and running the model:
m = Model()
