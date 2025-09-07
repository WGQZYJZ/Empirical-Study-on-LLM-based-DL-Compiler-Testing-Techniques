
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, ...)  # Apply dropout to the input tensor
        t2 = torch.rand_like(x1, ...)           # Generate a tensor with the same size as x1 filled with random numbers
        return t2


# Initializing the model
m = Model()
__input__ = torch.randn(1, 2, 2)

