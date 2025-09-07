
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.einsum('abc,cde->abef', (x1, x2))
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 5) # [batch size, n_channels, length]
x2 = torch.randn(3, 5, 7) # [n_channels, length, depth]
