
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        # Apply dropout to the input tensor.
        t = torch.nn.functional.dropout(x1, 0.5)
        # Generate a tensor with the same size as input_tensor filled with random numbers.
        t2 = torch.rand_like(t, dtype=torch.float32)
        return x + t


# Initializing the model