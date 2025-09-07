
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        v1 = torch.full([x.shape[0], 5], x * y, dtype=dtype) # Create a tensor filled with the specified value, with the specified shape and dtype.
        v2 = v1 + 1 # Add 1 to each element of the tensor.
        return v2

# Initializing the model
m = Model()


