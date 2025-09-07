
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)  # Concatenate tensors along a dimension
        v2 = v1.view(-1, 2 * 2)  # Reshape the concatenated tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5, 3)
x2 = torch.randn(5, 4, 2)
