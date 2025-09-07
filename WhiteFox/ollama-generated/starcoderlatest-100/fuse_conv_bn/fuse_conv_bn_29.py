
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        o1 = torch.nn.functional.conv2d(...)  # Apply convolution layer.
        o2 = torch.nn.functional.batch_norm(...)  # Apply batch normalization layer.
        output = o1 + o2   # Add the result of the two layers

        return output


# Initializing the model
m = Model()


def test(model):
    x = torch.randn(1, 3, 4)
    y = torch.randn(1, 6, 4)

    for i in range(100):
        # Run model on random input data
        output = model(x, y, torch.randn(2))

# Before fusing the convolution and batch normalization layers
test(m)


