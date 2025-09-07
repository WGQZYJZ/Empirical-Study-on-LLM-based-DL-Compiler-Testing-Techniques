
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(input_tensor, ...) # Apply linear transformation to the input tensor.
        return x2.permute(...) # Permute the output tensor from the linear transformation.


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
