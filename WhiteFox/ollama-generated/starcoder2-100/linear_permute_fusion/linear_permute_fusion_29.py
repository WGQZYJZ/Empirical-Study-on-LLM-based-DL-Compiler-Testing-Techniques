
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 3, 4, 5, 6, 7, 8)                                          # Permute the output of the linear function.
        return v2

# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(1, 3, 4, 5, 6, 7, 8)
__output__  = m(x1)

