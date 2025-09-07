
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=1)  # Concatenate two tensors along a dimension
        v = v.view(-1, 32 * 8 * 40)  # Reshape the concatenated tensor to [n * c1 * c2 * h1 * w1] where n is batch size and all other dimensions are multiplied together (e.g., batchsize * channel * height * width).
        v = torch.relu(v)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 2, 3, 40) # (bs, c1, h1, w1)
x2 = torch.randn(5, 3, 40)   # (bs, c2, h2)
