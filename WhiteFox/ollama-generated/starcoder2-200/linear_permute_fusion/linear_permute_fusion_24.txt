
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        v2  = v1.permute(0, 3, 2) # Permute the input tensor with 4 dimensions to 3 dimensions.
        return v2


# Initializing the model