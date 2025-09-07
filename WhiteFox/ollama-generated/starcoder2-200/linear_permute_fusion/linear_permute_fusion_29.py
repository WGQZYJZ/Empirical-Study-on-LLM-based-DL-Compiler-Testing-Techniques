
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self._weight)  # Apply the linear transformation to the input tensor with more than one dimension.
        v2 = v1.permute(-3, -1, -2) # Permute the output tensor from the linear function.
        return v2

# Initializing the model
m = Model()

