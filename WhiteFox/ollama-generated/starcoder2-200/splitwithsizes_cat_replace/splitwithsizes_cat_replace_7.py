
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Input to the model: x1 of shape (2048,)
        output = torch.split(x1, [50])  # Split `x1` into 3 tensors along the first dimension, each containing 50 elements
        return len(output)


m = Model()
__output_len__ = m(torch.randn(2048))

