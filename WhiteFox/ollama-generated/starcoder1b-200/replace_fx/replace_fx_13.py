
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0) # Dropout is not supported on a CPU device.
        t2 = torch.rand_like(t1, 0)        # Generate a tensor with the same size as input_tensor filled with random numbers
        return t2


# Initializing the model
m = Model()

