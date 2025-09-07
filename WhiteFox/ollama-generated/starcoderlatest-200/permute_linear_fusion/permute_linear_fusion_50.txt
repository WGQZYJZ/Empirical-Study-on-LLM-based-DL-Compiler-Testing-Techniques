
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(...)  # apply linear transformation to the permuted tensor
        return ...


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
