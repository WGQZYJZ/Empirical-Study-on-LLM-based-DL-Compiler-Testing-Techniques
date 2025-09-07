
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):  # x2, ... are the input tensor for this function
        v2 = self._conv_and_relu(x1)  # Invoke convolution and pointwise unary operation on x1
        return v2

    def _conv_and_relu(self, x1):
        v1 = self._linear_to_affine(x1)
        return torch.nn.functional.relu(v1)

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4, 2)
x2 = torch.randn(1, 3, 8, 3)
