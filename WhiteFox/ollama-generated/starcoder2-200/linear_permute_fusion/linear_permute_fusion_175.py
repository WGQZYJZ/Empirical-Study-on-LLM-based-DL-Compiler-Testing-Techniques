
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1.permute(-1, -3, -4) # Change the order of dimensions in the output tensor.
        return v2


# Initializing the model