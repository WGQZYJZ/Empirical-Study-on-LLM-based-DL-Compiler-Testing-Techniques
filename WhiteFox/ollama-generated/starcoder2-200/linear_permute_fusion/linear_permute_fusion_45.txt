
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, 42)
        v4 = v3.permute(0, 2, 1)
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 48) # An input tensor with more than two dimensions that meets the specified pattern.
