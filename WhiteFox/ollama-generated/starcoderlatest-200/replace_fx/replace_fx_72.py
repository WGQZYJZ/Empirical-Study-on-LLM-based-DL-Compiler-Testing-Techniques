
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(x1, dtype=torch.float) # Generate a tensor with the same size as input_tensor filled with random numbers
        v2 = torch.nn.functional.dropout(v1, p=0.25, training=True) # Apply dropout to the tensor generated in line 2
        return v2


# Initializing the model
m = Model()

