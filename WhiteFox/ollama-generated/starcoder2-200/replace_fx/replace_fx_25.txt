
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1  = torch.nn.functional.dropout(x1) # Apply dropout to the input tensor
        t2 = torch.rand_like(t1, dtype=x1.dtype) # Generate a tensor with the same size as t1 filled with random numbers
        return None


# Initializing the model