
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.dropout(x1, p=0.2) # Apply dropout to the input tensor
        return rand_like(v)  # Generate a tensor with the same size as v filled with random numbers


# Initializing and generating the inputs