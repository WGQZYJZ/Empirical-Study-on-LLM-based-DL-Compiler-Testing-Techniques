
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 3, 1, 4)
        return v2

# Initializing the model
m = Model()
__input_tensor__ = torch.randn(1, 2, 3)

