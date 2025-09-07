
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.conv1d(x1, self.linear.weight)  # Apply conv1d to the input tensor.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 5, 4)
__output__  = m(x1)

