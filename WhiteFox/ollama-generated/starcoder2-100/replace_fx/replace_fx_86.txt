
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.rand_like(x1, dtype=x1.dtype) # Generate a tensor with the same size as input_tensor filled with random numbers
        return v2

# Initializing the model
m = Model()

