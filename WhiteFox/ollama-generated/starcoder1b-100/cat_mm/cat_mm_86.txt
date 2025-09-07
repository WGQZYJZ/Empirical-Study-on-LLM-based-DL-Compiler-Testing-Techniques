
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dimension=None):  # In this example, `dimension=0` means concatenated along the batch axis, so the concatenation axis is `1`.
        result = torch.cat([x1 * x2, x1 * x2], dim=dimension)
        return result


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 4, 64, 64)
x2  = torch.randn(3, 4, 16, 16)
