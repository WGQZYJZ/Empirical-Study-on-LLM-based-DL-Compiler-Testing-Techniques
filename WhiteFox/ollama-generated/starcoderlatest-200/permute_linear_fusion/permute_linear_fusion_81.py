
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 3, 1).contiguous() # Add contiguous to preserve the dimension of input tensor in permute method. This may be unnecessary for your model definition, but it has been added here as an example.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 2, 5)
