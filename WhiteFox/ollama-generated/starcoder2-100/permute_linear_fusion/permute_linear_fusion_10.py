
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) # Apply a simple linear function on the input tensor.
        return v1


# Initializing the model