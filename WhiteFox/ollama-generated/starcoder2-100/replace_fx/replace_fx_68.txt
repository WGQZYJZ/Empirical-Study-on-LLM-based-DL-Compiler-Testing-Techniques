
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.dropout(x1) # Apply dropout to the input tensor
        v3  = torch.rand_like(v2)             # Generate a tensor with the same size as v2 filled with random numbers

        return v3


# Initializing the model
m = Model()


# Inputs to the model